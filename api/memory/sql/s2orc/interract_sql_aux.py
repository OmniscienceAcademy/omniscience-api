from typing import Dict, List

from api.core.containers import magAuthorId, prePaper0, prePaper1, s2orcId
from api.memory.sql.mag.mag_queries import (
    fetch_github,
    fetch_mag_authors_from_articles,
    fetch_paper_urls,
)
from api.memory.sql.omni_config_sql import session
from api.memory.sql.s2orc.columns import ArticleS2ORC


def list_to_sql_string(columns: List[str]) -> str:
    """input : ['xxx', 'yyy', ...]
    output : '"xxx", "yyy", ...'
    """
    r = ""
    for col in columns:
        r += '"' + col + '", '  # We add "" for postgre, but sqlite is indiferent
    r = r[:-2]
    return r


def clean_outbound_citations(papers: Dict[s2orcId, prePaper0]) -> None:
    # remove all the citations that are not in our database
    citations = []
    for paper in papers.values():
        citations += paper.outbound_citations  # type: ignore

    query = session.query(ArticleS2ORC.paper_id).filter(
        ArticleS2ORC.paper_id.in_(citations)
    )

    query = query.all()

    citations_in_database: List[s2orcId] = [row[0] for row in query]

    for paper in papers.values():
        paper.outbound_citations = list(
            set(paper.outbound_citations).intersection(  # type:ignore
                citations_in_database
            )
        )


def _get_urls(papers: Dict[s2orcId, prePaper0]) -> Dict[s2orcId, str]:
    mag_ids: List[int] = []
    for s2orc_id, paper in papers.items():
        mag_ids += paper.mag_ids

    paper_urls = fetch_paper_urls(mag_ids)
    s2orc_id_to_url: Dict[s2orcId, str] = {}
    for s2orc_id, article in papers.items():
        s2orc_id_to_url[s2orc_id] = ""
        for mag_paper_id in article.mag_ids:
            if paper_urls[mag_paper_id]:
                s2orc_id_to_url[s2orc_id] = paper_urls[mag_paper_id]
                break  # we use the first magId to give a non empty url
    return s2orc_id_to_url


def _get_mag_authors(
    papers: Dict[s2orcId, prePaper0]
) -> Dict[s2orcId, Dict[magAuthorId, str]]:
    mag_ids: List[int] = []
    for s2orc_id, paper in papers.items():
        mag_ids += paper.mag_ids
    mag_authors = fetch_mag_authors_from_articles(mag_ids)
    s2orc_id_to_authors: Dict[s2orcId, Dict[magAuthorId, str]] = {}
    for s2orc_id, article in papers.items():
        s2orc_id_to_authors[s2orc_id] = {}
        for mag_paper_id in article.mag_ids:
            if mag_authors[mag_paper_id]:
                s2orc_id_to_authors[s2orc_id] = mag_authors[mag_paper_id]
                break  # we use the first magId to give mag authors
    return s2orc_id_to_authors


def _get_github_urls(papers: Dict[s2orcId, prePaper0]) -> Dict[s2orcId, List[str]]:
    mag_id_to_s2orc_id = {}
    mag_ids: List[int] = []
    for s2orc_id, paper in papers.items():
        mag_ids += paper.mag_ids
        for mag_id in paper.mag_ids:
            mag_id_to_s2orc_id[mag_id] = s2orc_id
    githubs = fetch_github(mag_ids)
    s2orc_ids = list(papers.keys())
    s2orc_id_to_github_urls: Dict[s2orcId, List[str]] = {
        s2orc_id: [] for s2orc_id in s2orc_ids
    }
    for mag_id in githubs.keys():
        s2orc_id = mag_id_to_s2orc_id[mag_id]
        s2orc_id_to_github_urls[s2orc_id] += githubs[mag_id]

    return s2orc_id_to_github_urls


def add_mag_columns(papers: Dict[s2orcId, prePaper0]) -> Dict[s2orcId, prePaper1]:

    s2orc_id_to_github_urls = _get_github_urls(papers)

    s2orc_id_to_url = _get_urls(papers=papers)

    s2orc_id_to_authors = _get_mag_authors(papers=papers)

    papers1: Dict[s2orcId, prePaper1] = {}
    for s2orc_id, paper0 in papers.items():
        github_urls = s2orc_id_to_github_urls[s2orc_id]
        paper_url = s2orc_id_to_url[s2orc_id]
        mag_authors = s2orc_id_to_authors[s2orc_id]

        papers1[s2orc_id] = prePaper1(
            paper=paper0,
            github_urls=github_urls,
            mag_authors=mag_authors,
            paper_url=paper_url,
        )
    return papers1

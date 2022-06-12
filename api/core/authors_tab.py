from typing import Dict, List, Tuple

from sqlalchemy import func

from api.core.containers import Paper, magAuthorId, s2orcId
from api.memory.sql.mag.mag_schema import PaperAuthorAffiliations, PaperReferences
from api.memory.sql.omni_config_sql import session
from api.specs import AUTHOR_TAB_SIZE, MAX_N_ARTICLES_FOR_AUTHOR_EXPLORATION


def _get_surrounding_authors(
    articles: Dict[s2orcId, Paper]
) -> List[Tuple[magAuthorId, int]]:
    # Returns a List of Tuples of the form:
    # (mag author id X,
    # number of articles Y cited by at least one of the
    # articles given in parameters, where X is author of Y)

    # (maybe ? TODO: include the authors of articles given in parameters, to avoid
    # having to add them in python later, cf function `find_best_authors_in`)
    assert len(articles) <= MAX_N_ARTICLES_FOR_AUTHOR_EXPLORATION
    mag_article_ids: List[int] = []
    for article in articles.values():
        mag_article_ids += article.mag_ids

    mag_article_ids = mag_article_ids[:4]

    query = (
        session.query(
            PaperAuthorAffiliations.AuthorId,
            func.count(PaperReferences.paperreferenceid),
        )
        .join(
            PaperReferences,
            PaperReferences.paperreferenceid == PaperAuthorAffiliations.PaperId,
        )
        .group_by(PaperAuthorAffiliations.AuthorId)
        .filter(PaperReferences.paperid.in_(mag_article_ids))
    )
    query = query.all()

    return query


def get_best_articles_for_author_exploration(
    articles: Dict[s2orcId, Paper]
) -> Dict[s2orcId, Paper]:

    s2oorc_ids_and_scores = [(id, articles[id].general_score) for id in articles]
    s2oorc_ids_and_scores_sorted = sorted(
        s2oorc_ids_and_scores, key=lambda x: x[1], reverse=True
    )
    s2oorc_ids_sorted = [id_score[0] for id_score in s2oorc_ids_and_scores_sorted]
    s2oorc_ids_sorted = s2oorc_ids_sorted[:MAX_N_ARTICLES_FOR_AUTHOR_EXPLORATION]
    return {id: articles[id] for id in s2oorc_ids_sorted}


def find_best_authors_in(papers: Dict[s2orcId, Paper]) -> List[magAuthorId]:
    # mag_author_id -> ratio of written articles in {`articles`} union
    # {articles cited by `articles`}
    # (actually, this not totally true because of intersection between
    # the 2 sets ... to obtain the real number, we should to it fully by
    # sql, as mentionned in the comment in _get_surrounding_authors)
    author_occurences: Dict[int, int] = {}
    total_n_occurences = 0

    def add_occurence(mag_author_id: int, occ_to_add: int) -> None:
        nonlocal total_n_occurences
        total_n_occurences += occ_to_add
        if mag_author_id in author_occurences:
            author_occurences[mag_author_id] += occ_to_add
        else:
            author_occurences[mag_author_id] = occ_to_add

    for paper in papers.values():
        for mag_author_id in paper.mag_authors.keys():
            add_occurence(mag_author_id, 1)

    # we limit ourselves otherwise SQL bugs
    articles_to_explore = get_best_articles_for_author_exploration(papers)
    surrounding_authors = _get_surrounding_authors(articles_to_explore)

    for mag_author_id, occ_to_add in surrounding_authors:
        add_occurence(mag_author_id, occ_to_add)
    best_author_ids = sorted(
        list(author_occurences.keys()),
        key=lambda author_id: author_occurences[author_id],
    )[::-1]
    if len(best_author_ids) > AUTHOR_TAB_SIZE:
        best_author_ids = best_author_ids[0:AUTHOR_TAB_SIZE]
    return best_author_ids

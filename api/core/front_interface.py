from typing import Any, Dict, List

from api.core.containers import Paper, YearRange, prePaper2, s2orcId
from api.core.wikipedia import fetch_wikipedia


def serialize_paper_for_front(paper: Paper) -> Dict[str, Any]:
    res = {}
    res["id"] = paper.s2orc_id
    res["score"] = paper.general_score
    res["year"] = paper.year
    res["nbInCitations"] = paper.nb_inbound_citations
    res["nbOutCitations"] = paper.nb_outbound_citations
    res["title"] = paper.title
    res["github_urls"] = paper.github_urls
    res["tags"] = paper.tags
    return res


def _format_author_name(author_name: str) -> str:
    sub_names = author_name.split()
    formated_name = ""
    for sub_name in sub_names[:-1]:
        formated_name += sub_name[0] + ". "
    formated_name += sub_names[-1]
    return formated_name


def _format_paper(paper: prePaper2) -> Dict[str, Any]:
    return {
        "id": paper.s2orc_id,
        "title": paper.title,
        "year": paper.year,
        "vanue": paper.venue,
        "github_urls": paper.github_urls,
        "tags": paper.tags,
        "paperAbstract": paper.abstract,
        "nbInCitations": paper.nb_inbound_citations,
        "nbOutCitations": paper.nb_outbound_citations,
        "s2Url": paper.s2_url,
        "journalName": paper.journal,
        "language": "un",
        "magId": paper.mag_ids[0] if paper.mag_ids else None,
        "tldr": paper.tldr,
        "question": paper.question,
        "pdfUrls": [paper.paper_url],
        "authors": [
            [mag_author_id, _format_author_name(author_name)]
            for mag_author_id, author_name in paper.mag_authors.items()
        ],
    }


def get_formated_articles(papers: Dict[s2orcId, prePaper2]) -> List[Dict[str, Any]]:
    formated_articles = []
    for paper in papers.values():
        formated_articles.append(_format_paper(paper))
    return formated_articles


def get_error_article(id_: int):
    error_article = {
        "id": id_,
        "title": "Sorry, no results found.",
        "paperAbstract": "Sorry, you can try to reformulate your query.",
        "authors": [],
        "nbInCitations": 404,
        "nbOutCitations": 404,
        "year": 404,
        "s2Url": "https://omniscience.academy/",
        "sources": [],
        "pdfUrls": ["https://omniscience.academy/"],
        "venue": "OmniScience and Co",
        "journalName": "OmniScience and Co",
        "journalVolume": "404",
        "journalPages": "404",
        "doi": "",
        "doiUrl": "",
        "pmid": "",
        "fieldsOfStudy": ["Omniscience"],
        "magId": "",
        "s2PdfUrl": "",
        "entities": [],
        "tldr": "Sorry, you can try to reformulate your query.",
        "tags": [],
        "top_articles_citing": [],
        "top_articles_cited": [],
        "similar_articles_not_cited_by_us": [],
        "similar_articles": [],
    }
    return error_article


def get_serialized_results_error(query: str) -> Dict[str, Any]:
    serialized_results = {
        "articles": [get_error_article(4040000000000000000)],
        "user_query": "Error: " + query,
        "graph": {},
        "questions": [],
        "main_answer": None,
        "wikipedia": fetch_wikipedia(
            wiki_url="https://en.wikipedia.org/wiki/Meaning_of_life"
        ),  # 5 %
        "related_search": [],
        "yearRange": YearRange(startYear=1900, endYear=2022),
        "extrYearRange": YearRange(startYear=1900, endYear=2022),
    }
    return serialized_results


def get_formated_serialized_results(
    articles: List[Dict[str, Any]],
    user_query: str,
    graph: Dict[str, Any],
    questions: List[Any],
    main_answer: Dict[str, Any],
    wikipedia: Dict[str, Any],
    related_search: List[str],
    best_authors: List[int],
    yearRange: YearRange,
    extrYearRange: YearRange,
) -> Dict[str, Any]:
    serialized_results = {
        "articles": articles,
        "user_query": user_query,
        "graph": graph,
        "questions": questions,
        "main_answer": main_answer if main_answer else None,
        "wikipedia": wikipedia if wikipedia else None,
        "related_search": related_search,
        "best_authors": best_authors,
        "yearRange": yearRange,
        "extrYearRange": extrYearRange,
    }
    return serialized_results

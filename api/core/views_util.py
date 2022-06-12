import json
import secrets

# from time import time
from typing import Any, Dict, List

from django.utils import timezone

from api.core.containers import Paper, YearRange, prePaper2, s2orcId
from api.core.front_interface import (
    get_formated_serialized_results,
    serialize_paper_for_front,
)
from api.core.graph import create_graph
from api.core.questions import create_questions
from api.core.tags import get_wiki_url
from api.core.wikipedia import fetch_wikipedia
from api.memory.faiss import call_abstract_faiss, call_title_faiss
from api.memory.sql.mag.mag_queries import fetch_fields_of_study_by_ids
from api.models import SwipeResults
from api.services.language_correction import call_language_corrector_api
from api.services.spacy import find_language
from api.specs import MIN_SCORE_MAIN_ANSWER, N_RELATED_TOPICS, N_SIMILAR_ARTICLES


def filter_article_content(paper: prePaper2) -> None:
    """Delete heavy fields and publicity."""

    paper.outbound_citations = []
    paper.inbound_citations = []

    # Black list url
    if "petplaygroun" in paper.paper_url:
        paper.paper_url = ""


def get_corrected_user_query(user_query: str) -> str:
    if len(user_query) > 250:
        user_query = user_query[:250]  # avoid DDOS

    language_and_score = find_language(user_query)
    language = language_and_score["language"]
    score = language_and_score["score"]
    _ = score

    if language == "en":
        return call_language_corrector_api(user_query=user_query)
    else:
        return user_query


def get_serialized_results(
    user_query: str,
    papers: Dict[s2orcId, Paper],
    best_authors: List[int],
    yearRange: YearRange,
    extrYearRange: YearRange,
) -> Dict[str, Any]:

    articles = [serialize_paper_for_front(paper) for paper in papers.values()]
    graph = create_graph(papers=papers)
    main_answer = get_main_answer(user_query)
    questions = create_questions(best_articles=papers, user_query=user_query)
    df_magId_field = fetch_fields_of_study_by_ids(
        mag_ids=[paper.mag_ids for paper in papers.values()]
    )
    related_search = get_related_search(df_magId_field)
    wiki_url = get_wiki_url(df_magId_field, papers, user_query)
    wikipedia = fetch_wikipedia(wiki_url)

    return get_formated_serialized_results(
        articles=articles,
        user_query=user_query,
        graph=graph,
        best_authors=best_authors,
        main_answer=main_answer,
        questions=questions,
        related_search=related_search,
        wikipedia=wikipedia,
        yearRange=yearRange,
        extrYearRange=extrYearRange,
    )


def save_results(serialized_results: Dict[str, Any],) -> str:
    # TODO : add a session_id in the model
    swipe_session_token = secrets.token_hex(10)

    swipe_results = SwipeResults(
        # TODO : to rename
        id_swipe_session=swipe_session_token,
        pub_date=timezone.now(),
        query=serialized_results["user_query"],  # redondant but necessary
        serialized_results=json.dumps(serialized_results),
    )

    swipe_results.save()
    return swipe_session_token


def fetch_similar_papers_ids(paper: prePaper2) -> List[int]:
    similar_ids_and_scores, extrYearRange = call_title_faiss(
        paper.title, 1 + N_SIMILAR_ARTICLES, yearRange={"startYear": 0, "endYear": 2030}
    )
    similar_ids = list(similar_ids_and_scores.keys())
    if paper.s2orc_id in similar_ids:
        similar_ids.remove(paper.s2orc_id)
    return similar_ids


def get_related_search(df_magId_field) -> List[str]:
    """Takes the most occurence fieldodstudies and sort by level."""
    # df_magId_field.to_csv("/tmp/df_magId_field.csv")
    df = df_magId_field

    # Create df_fields with a column occurence and a column level
    res = df["fieldofstudy"].value_counts()
    df_fields = df.drop_duplicates(subset=["fieldofstudy"])
    df_fields = df_fields.merge(res, left_on="fieldofstudy", right_index=True)
    df_fields.rename(columns={"fieldofstudy_y": "occurence"}, inplace=True)

    # take the best 10 and sort by level
    df_best_fields = df_fields.sort_values(by=["occurence"], ascending=False).head(
        N_RELATED_TOPICS
    )
    df_sorted_level = df_best_fields.sort_values(by=["level"], ascending=True)
    return list(df_sorted_level.fieldofstudy)


def get_main_answer(user_query: str) -> Dict[str, Any]:
    # we assume that the user query is like a question
    call_result = call_abstract_faiss(user_query)
    if not call_result:
        return {}
    if call_result["score"] < MIN_SCORE_MAIN_ANSWER:
        return {}
    return {"answer": call_result["answer"], "article_id": call_result["paper_id"]}

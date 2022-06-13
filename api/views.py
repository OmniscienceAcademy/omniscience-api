import json
import os

import pandas as pd
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.core.authors_tab import find_best_authors_in
from api.core.containers import Paper, YearRange
from api.core.front_interface import (
    get_error_article,
    get_formated_articles,
    get_serialized_results_error,
)
from api.core.search_engine import search_papers
from api.core.tags import add_fields_of_studies_tag
from api.core.views_util import (
    fetch_similar_papers_ids,
    filter_article_content,
    get_corrected_user_query,
    get_serialized_results,
    save_results,
)
from api.memory.faiss import call_question_faiss, call_title_faiss, util_call_api
from api.memory.sql.mag.mag_queries import (
    fetch_authors,
    fetch_authors_by_ids,
    fetch_authors_of_field_of_study2,
    fetch_field_of_study_children,
    fetch_fields_of_study,
    fetch_fields_of_study_containing_subword,
    fetch_fields_of_study_level_0,
    fetch_github,
    fetch_main_papers_of_field_of_study,
    fetch_resources_field_of_study,
)
from api.memory.sql.s2orc.interract_sql import fetch_papers, get_most_cited_ids
from api.models import SwipeResults
from api.specs import MAX_N_TOP_ARTICLES_CITED_TO_SHOW
from config.settings import DEBUG, IS_PROD


def search_title(request: HttpRequest, user_query):
    """Return the results of the main search bar."""
    # For now only in economy.

    # dict s2orc id -> faiss similarity
    similarities, extrYearRange = call_title_faiss(
        user_query, k=50, yearRange={"startYear": 0, "endYear": 2030}
    )
    articles = {
        {"s2orc_id": s2orc_id, "similarity": similarity}
        for s2orc_id, similarity in similarities.items()
    }
    return JsonResponse({"articles": articles}, json_dumps_params={"indent": 2})


def search_abstract(request: HttpRequest, string):
    """DEPRECATED"""
    return JsonResponse({"error": "Deprecated"})


def index(request: HttpRequest):
    version = "production" if IS_PROD else "developement"
    return JsonResponse(
        {"status": f"Welcome to omniscience api. This is the {version} version."}
    )


def get_article_by_id(request: HttpRequest, paper_id):
    """paper_id : article id. Used for article/paper_id urls on the front."""
    try:
        paper = fetch_papers(ids=[paper_id], use_only_python_lists=True)[paper_id]

        similar_papers_ids = fetch_similar_papers_ids(paper)

        most_cited_ids = get_most_cited_ids(
            ids=paper.outbound_citations, N=MAX_N_TOP_ARTICLES_CITED_TO_SHOW
        )
        # article["top_articles_citing"] = get_most_cited_articles(
        #     ids=article[Columns.inCitations], N=0
        # ) Not usefull for now

        paper = Paper(paper=paper, general_score=0)  # TODO virer ca

        add_fields_of_studies_tag(paper)  # type: ignore

        filter_article_content(paper)

        formated_article = get_formated_articles({paper.s2orc_id: paper})[0]
        formated_article["similar_articles"] = similar_papers_ids
        formated_article["top_articles_cited"] = most_cited_ids
        formated_article["similar_articles_not_cited_by_us"] = []
        formated_article["top_articles_citing"] = []

    except AssertionError as e:
        print(e)
        formated_article = get_error_article(paper_id)

    return JsonResponse(formated_article, json_dumps_params={"indent": 2})


def top_articles(request: HttpRequest):
    """Top 100 articles from economy."""
    df = pd.read_excel("misc/top_articles.xlsx")
    ids = df["id"].to_list()

    return JsonResponse({"top_articles": ids}, json_dumps_params={"indent": 2})


@csrf_exempt
def get_articles_by_id(request: HttpRequest):
    """Post request containing list of ids.

    Warning : return the list of unordered articles.
    The order is not preserved.
    """
    if request.method != "POST":
        return JsonResponse({"error": "query must be POST request."})
    dict = json.loads(request.body)
    ids = dict["ids"]
    ids = [int(id) for id in ids if id]

    try:
        # usefull for bold
        query = dict["query"] if "query" in dict else None
        return_questions = (
            dict["return_questions"] if "return_questions" in dict else False
        )
        return_citations = (
            dict["return_citations"] if "return_citations" in dict else False
        )

        papers = fetch_papers(
            ids=ids,
            use_only_python_lists=True,
            user_query=query,
            return_questions=return_questions,
        )

        if not return_citations:
            for article in papers.values():
                filter_article_content(article)

        formated_articles = get_formated_articles(papers)

    except Exception as e:
        print(e)
        formated_articles = [get_error_article(id) for id in ids]
    return JsonResponse(
        {"articles": formated_articles}, json_dumps_params={"indent": 2}
    )


class DebugEnablingError(Exception):
    pass


def get_directs_results(
    request: HttpRequest, user_query: str, min_year: int, max_year: int
):
    try:
        yearRange = YearRange(startYear=min_year, endYear=max_year)

        papers, extrYearRange = search_papers(
            user_query=user_query, yearRange=yearRange
        )

        # We correct yearRange
        yearRange["startYear"] = max(extrYearRange["startYear"], yearRange["startYear"])
        yearRange["endYear"] = min(extrYearRange["endYear"], yearRange["endYear"])

        min_year = int(min_year) if min_year else 0

        papers = {
            id_: paper
            for id_, paper in papers.items()
            if paper.year and paper.year >= min_year
        }

        best_authors = find_best_authors_in(papers)

        if len(papers) < 1:
            return JsonResponse(
                {"error": "There is not enough matching papers in our database."}
            )

        serialized_results = get_serialized_results(
            user_query, papers, best_authors, yearRange, extrYearRange
        )
    except Exception as e:
        print(e)
        if DEBUG:
            raise e
        serialized_results = get_serialized_results_error(user_query)

    swipe_session_token = save_results(serialized_results)  # 2 %

    return JsonResponse({"swipe_session_token": swipe_session_token})


def get_results_swipe(request: HttpRequest, swipe_session_token: str):
    """Return the results stored in the db."""
    try:
        swipe_results = SwipeResults.objects.get(pk=swipe_session_token)
    except SwipeResults.DoesNotExist:
        return JsonResponse({"error": "swipe_session_token does not exists."})

    serialized_results = swipe_results.serialized_results
    res = json.loads(serialized_results)

    return JsonResponse(res, json_dumps_params={"indent": 2})


def run_tests(request: HttpRequest):
    """Run tests."""
    try:
        os.system("python manage.py test")
    except Exception as e:
        return JsonResponse({"error": str(e)})

    return JsonResponse({"success": "ok"})


@csrf_exempt
def get_fields_of_study_by_ids(request: HttpRequest):
    """Return the fields of study corresponding to the ids."""
    ids = request.POST.getlist("ids")
    int_ids = [int(id) for id in ids]
    df_fields_of_study = fetch_fields_of_study(int_ids)
    return JsonResponse(
        {"fields_of_study": df_fields_of_study.to_dict(orient="records")}
    )


def get_children_of_field_of_study_id(request: HttpRequest, field_of_study_id: int):
    """Return the children fields of study corresponding to the ids."""
    fields_of_study_ids = fetch_field_of_study_children(field_of_study_id)
    df_fields_of_study = fetch_fields_of_study(fields_of_study_ids)
    return JsonResponse(
        {"child_fields_of_study": df_fields_of_study.to_dict(orient="records")}
    )


def get_fields_of_study_level_0_info(request: HttpRequest):
    """Return the fields of study corresponding to the ids."""
    fields_of_study_ids = fetch_fields_of_study_level_0()
    df_fields_of_study = fetch_fields_of_study(fields_of_study_ids)
    return JsonResponse(
        {"fields_of_study": df_fields_of_study.to_dict(orient="records")}
    )


def search_fields_of_study(request: HttpRequest, query: str):
    """Return the fields of study corresponding to the ids."""
    fields_of_study_ids = fetch_fields_of_study_containing_subword(query)
    df_fields_of_study = fetch_fields_of_study(fields_of_study_ids)
    return JsonResponse(
        {"fields_of_study": df_fields_of_study.to_dict(orient="records")}
    )


def get_authors_of_field_of_study(request: HttpRequest, field_of_study_id: int):
    """Return the fields of study corresponding to the ids."""
    ids = fetch_authors_of_field_of_study2(field_of_study_id)
    df = fetch_authors_by_ids(mag_author_ids=ids)
    return JsonResponse({"authors": df.to_dict(orient="records")})


# mag id
@csrf_exempt
def get_authors_by_ids(request: HttpRequest):
    """Return the fields of study corresponding to the ids."""
    if request.method != "POST":
        return JsonResponse({"error": "query must be POST request."})
    dict = json.loads(request.body)
    ids = dict["ids"]
    ids = [int(id) for id in ids if id]
    df = fetch_authors_by_ids(mag_author_ids=ids)
    return JsonResponse({"authors": df.to_dict(orient="records")})


def get_author_by_id(request: HttpRequest, author_id: int):
    """Return the fields of study corresponding to the ids."""
    df = fetch_authors_by_ids([author_id])
    return JsonResponse(
        {
            "author": df.to_dict(orient="records")[0],
            "top_articles_cited_ids": [9166388],
            "recent_articles_ids": [9166388],
        }
    )


def get_top_github_by_field_of_study(request: HttpRequest, field_of_study_id: int):
    """Return the fields of study corresponding to the ids."""
    _ = field_of_study_id
    res = fetch_github([])  # TODO
    return JsonResponse({"githubs": res})


def get_search_authors(request: HttpRequest, query: str):
    """Return the fields of study corresponding to the ids."""
    df = fetch_authors(query)
    return JsonResponse({"authors": df.to_dict(orient="records")})


def get_main_papers_of_field_of_study(request: HttpRequest, field_of_study_id: int):
    """Return the fields of study corresponding to the ids."""
    df = fetch_main_papers_of_field_of_study(field_of_study_id)
    return JsonResponse({"main_papers": df.to_dict(orient="records")})


def get_resources_field_of_study(request: HttpRequest, field_of_study_id: int):
    """Return the fields of study corresponding to the ids."""
    df = fetch_resources_field_of_study(field_of_study_id)
    return JsonResponse({"resources": df.to_dict(orient="records")})


def get_autocompletion(request: HttpRequest, user_query: str):
    """Return the fields of study corresponding to the ids."""
    correct = get_corrected_user_query(user_query)

    questionings = call_question_faiss(correct, k=5)

    titles = util_call_api(
        "title", user_query=correct, retriever_q=10, correct_cossim=None
    )
    titles = [
        {"type": "📜", "name": doc["content"]} for doc in titles["query"]["documents"]
    ]
    questions = [{"type": "❓", "name": q["question"]} for q in questionings][:0]

    if correct.strip() == user_query.strip():
        res = [{"type": "", "name": user_query}] + questions + titles
    else:
        res = (
            [{"type": "", "name": user_query}, {"type": "😘", "name": correct}]
            + titles
            + questions
        )

    for i in range(len(res)):
        res[i]["id"] = i  # type:ignore

    df = pd.DataFrame(res)

    # df.to_csv("/tmp/df_suggestions.csv")

    df["name_"] = df["name"].str.lower()
    df["name_"] = df["name_"].str.strip('!"#$%&*+,-./:;<=>?@[^_`{|}~ ' + "'")
    df.drop_duplicates(subset=["name_", "type"], inplace=True)

    return JsonResponse({"autocompletion": df.to_dict(orient="records")})

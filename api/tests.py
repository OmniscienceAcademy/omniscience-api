"""Test suite.

To execute :
source djenv/bin/activate
./manage.py test

To execute only a function (for test) :
./manage.py test api.tests.SwipeTests.test_swipe_profile
"""
import json

from django.http import HttpRequest
from django.test import Client
from line_profiler import LineProfiler
from snapshottest.django import TestCase
from tqdm import tqdm

import api.memory.sql.s2orc.interract_sql as interract_sql
from api.memory.faiss import call_title_faiss, put_in_bold_answer
from api.memory.sql.clean_fetching import clean_abstract
from api.services.spacy import put_in_bold_matching_words
from api.views import get_article_by_id
from misc.random_query import get_random_query
from misc.stress_tests import query_examples


class DebugTests(TestCase):

    # used only for debugging, not to test code before each commit
    def _emile_teste(self):
        pass


class BasicRoutesTests(TestCase):
    def test_get_article_by_id(self):
        """python manage.py test api.tests.BasicRoutesTests.test_get_article_by_id"""
        print("test_get_article_by_id")
        # id = "90382b9ec93c001dfc81f87c11604e99fe570582"
        # it seems this id is midding from Postgres, but not from sqlite !!!

        id = 153662531
        res = get_article_by_id(HttpRequest(), paper_id=id)
        res_json = json.loads(res.content)
        self.assertMatchSnapshot(res_json)

    def test_get_articles(self):
        """python manage.py test api.tests.BasicRoutesTests.test_get_articles"""
        print("test_get_articles")

        # coming from https://www.omniscienceapi.com:4430/get-article-by-id/d70c5c1edd8533d716cffae33ba6d902646680ed/ # noqa: E501
        ids = [
            144555080,
            154671520,
            153662531,
            153666201,
            153666223,
            153667575,
            153669883,
            146157251,
            144551922,
            18988104,
        ]
        _ = interract_sql.fetch_papers(ids=ids)
        print(_)
        # self.assertMatchSnapshot(_)

    def test_faiss_articles_with_infos(self):
        print("test_faiss_articles_with_infos")
        c = Client()
        response = c.get("/faiss_articles_with_infos/bread/5/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def test_get_fields_of_study_level_0(self):
        print("test_get_fields_of_study_level_0")
        c = Client()
        response = c.get("/get_fields_of_study_level_0/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def test_get_fields_of_study_by_ids(self):
        print("test_get_fields_of_study_by_ids")
        c = Client()
        response = c.get("/get_fields_of_study_by_ids/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def test_get_field_of_study_children(self):
        print("test_get_field_of_study_children")
        c = Client()
        response = c.get("/get_field_of_study_children/40700/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def test_search_fields_of_study(self):
        c = Client()
        response = c.get("/search_fields_of_study/economics/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def get_authors_of_field_of_study(self):
        print("get_authors_of_field_of_study")
        c = Client()
        response = c.get("/get_authors_of_field_of_study/2992352532/0/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def get_authors_of_field_of_study_french(self):
        print("get_authors_of_field_of_study_french")
        c = Client()
        response = c.get("/get_authors_of_field_of_study/2992352532/1/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    """
    def test_get_top_github_by_field_of_study(self):
        # too long
        print("test_get_top_github_by_field_of_study")
        c = Client()
        response = c.get("/get_top_github_by_field_of_study/12843/")
        res_json = json.loads(response.content)
        self.assertMatchSnapshot(res_json)
    """

    """
    def test_get_search_authors(self):
        # Seems too long
        c = Client()
        response = c.get("/get_search_authors/conflict/")
        res_json = json.loads(response.content)
        self.assertMatchSnapshot(res_json)
    """

    def test_get_resources_field_of_study(self):
        print("test_get_resources_field_of_study")
        c = Client()
        response = c.get("/get_resources_field_of_study/40700/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def test_get_main_papers_of_field_of_study(self):
        print("test_get_main_papers_of_field_of_study")
        c = Client()
        response = c.get("/get_main_papers_of_field_of_study/2779366248/")
        res_json = json.loads(response.content)  # type: ignore
        self.assertMatchSnapshot(res_json)

    def _test_get_articles_profile(self):

        lp = LineProfiler()

        lp_wrapper = lp(self.test_get_articles)
        lp.add_function(interract_sql.fetch_papers)

        lp_wrapper()  # type: ignore
        lp.print_stats()


class QueryTests(TestCase):
    def _test_query(self, query, c):
        response = c.get(f"/get-direct-results/{query}/0/2020/")
        session_token = json.loads(response.content)[  # type: ignore
            "swipe_session_token"
        ]
        response = c.get(f"/get-results-swipe/{session_token}/")
        articles = json.loads(response.content)["articles"]  # type: ignore
        assert len(articles) >= 1
        assert articles[0]["title"] != "Sorry, no results found."
        # self.assertMatchSnapshot(articles)

    def test_single_query(self):
        """python manage.py test api.tests.QueryTests.test_single_query"""
        print("test single query")
        c = Client()
        query = query_examples[83]  # "Deep learning and Machine learning"
        self._test_query(query, c)

    def test_multiple_queries(self):
        print("test multiple queries")
        c = Client()
        for query in tqdm(query_examples):
            self._test_query(query, c)

    def test_multiple_random_queries(self):
        print("test multiple random queries")
        c = Client()
        for _ in tqdm(range(100)):
            random_query = get_random_query()
            self._test_query(random_query, c)


class MiscTests(TestCase):
    def _testFaissIsInDB(self, query):
        faiss_ids_and_scores, extrYearRange = call_title_faiss(
            query, 100, yearRange={"startYear": 0, "endYear": 2030}
        )
        faiss_ids = set(faiss_ids_and_scores.keys())
        sql_papers = interract_sql.fetch_papers(list(faiss_ids))
        sql_ids = set(sql_papers.keys())
        assert sql_ids == faiss_ids

    def testFaissIsInDB(self):
        for query in query_examples:
            self._testFaissIsInDB(query)

    def test_bold(self):
        res = put_in_bold_matching_words(abstract="This is a test.", user_query="test")
        self.assertMatchSnapshot(res)

        res = put_in_bold_matching_words(
            "This is the Economy of conflicts", "Economy of conflict"
        )
        self.assertMatchSnapshot(res)

        res = put_in_bold_matching_words(
            "Inflation in lebanon and in France", "Inflation in Lebanon"
        )
        self.assertMatchSnapshot(res)

        res = put_in_bold_matching_words(
            "Inflation in  lebanon and in France", "Inflation  in Lebanon"
        )
        self.assertMatchSnapshot(res)

    def test_clean_abstract(self):
        """python manage.py test api.tests.MiscTests.test_clean_abstract"""
        abstract = " Abstract This is a test."
        abstract = clean_abstract(abstract)
        self.assertEqual(abstract, " This is a test.")

        abstract = " This is a test."
        abstract = clean_abstract(abstract)
        self.assertEqual(abstract, " This is a test.")

        abstract_ = " This is a test" * 10 + "Abstract abcd"
        abstract = clean_abstract(abstract_)
        self.assertEqual(abstract, abstract_)

    def test_bold_answer(self):
        """python manage.py test api.tests.MiscTests.test_bold_answer"""
        abstract = "Neurodiversity, or ND, refers to variation in the human brain regarding sociability, learning, attention, mood and other mental functions in a non-pathological sense. It was coined in 1998 by sociologist Judy Singer, who helped popularize the concept along with journalist Harvey Blume. It emerged as."  # noqa

        answer = "variation in the human brain regarding sociability, learning"
        bold = put_in_bold_answer(abstract, answer)
        print(bold)

        answer = "Neurodiversity, or ND, refers to variation in the human brain regarding sociability, learning, attention, mood and other mental functions in a non-pathological sense. It was coined in 1998"  # noqa
        bold = put_in_bold_answer(abstract, answer)
        print(bold)

        answer = " It emerged as"
        bold = put_in_bold_answer(abstract, answer)
        print(bold)

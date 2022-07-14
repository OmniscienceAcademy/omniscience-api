from dataclasses import dataclass
from typing import Any, Dict, List

import api.memory.sql.omni_config_sql as omni_config_sql
from api.core.containers import s2orcId
from api.memory.sql.s2orc.columns import QuestionAndTldr
from api.specs import MIN_COS_SIM_ARTICLE_QUESTION


@dataclass
class QA:
    question: str
    answer: str  # == tldr (currently)
    paper_id: int
    score: float  # == 1 - cos_sim(question, answer)

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "article_id": self.paper_id,
            "score": self.score,  # 1 = best, -1 = worst
        }

    def to_dict_front(self):
        return {"answer": self.answer, "article_id": self.paper_id}

    def __eq__(self, qa) -> bool:
        return self.paper_id == qa.paper_id

    def fill_missing(self, articles: Dict[int, Dict[str, Any]]) -> bool:
        assert self.paper_id
        # the questions are already given by FAISS, no need of sql here
        assert self.question

        # articles has been returned by sql, we use it to fill the tldr + cos sim

        if self.paper_id not in articles.keys():
            print(
                "WARNING, an article id from Faiss is not in the DB: "
                + str(self.paper_id)
            )
            return False

        self.answer = articles[self.paper_id]["tldr"]
        self.score = articles[self.paper_id]["cossim_tldr_question"]
        return True


@dataclass
class TopQuestions:
    """Class for keeping track of an item in inventory."""

    best_qa: QA
    q_and_a: List[QA]  # the other QA contains the main

    def to_dict(self):
        return {
            "best_question": self.best_qa.to_dict(),
            "q_and_a": [qa.to_dict() for qa in self.q_and_a],
        }


def add_missing_entries(all_top_questions: Dict[int, TopQuestions]) -> None:
    # There are some papers that we have not seen before (as candidates papers of swipes)
    # and that are part of the articles answering the questions. These articles have been
    # fetched with FAISS anf thus we lack some sql data. To simplify a bit, we will query
    # SQL for all the articles present in all_top_questions, even if we knwo already the
    # entries we are looking for (in GENERAL_VALUES)
    ids = []
    for top_questions in all_top_questions.values():
        ids.append(top_questions.best_qa.paper_id)
        for qa in top_questions.q_and_a:
            ids.append(qa.paper_id)
    articles = _fetch_questions(ids=ids)
    for top_questions in list(all_top_questions.values()):
        # normalement chaque article relié à une question principale est dans sql
        assert top_questions.best_qa.fill_missing(articles)
        qa_to_remove: List[QA] = []
        for qa in top_questions.q_and_a:
            if not qa.fill_missing(articles):
                qa_to_remove.append(qa)  # id dans faiss mais pas dans sql
        for qa in qa_to_remove:
            top_questions.q_and_a.remove(qa)


def _fetch_questions(ids: List[int]) -> Dict[s2orcId, Dict[str, Any]]:
    query = omni_config_sql.session.query(
        QuestionAndTldr.paper_id,
        QuestionAndTldr.question,
        QuestionAndTldr.tldr,
        QuestionAndTldr.cossim_tldr_question,
    ).filter(QuestionAndTldr.paper_id.in_(ids))
    articles: Dict[int, Dict[str, Any]] = {}
    for row in query.all():
        s2orc_id = row[0]
        articles[s2orc_id] = {"paper_id": s2orc_id}
        articles[s2orc_id]["question"] = row[1]
        articles[s2orc_id]["tldr"] = row[2]
        articles[s2orc_id]["cossim_tldr_question"] = row[3]

    return articles


def fetch_questions(ids: List[int]) -> Dict[int, TopQuestions]:
    articles = _fetch_questions(ids)
    all_top_questions: Dict[int, TopQuestions] = {}

    for paper_id, article in articles.items():
        question = article["question"]
        cossim_tldr_question = article["cossim_tldr_question"]
        if cossim_tldr_question < MIN_COS_SIM_ARTICLE_QUESTION:
            continue
        best_qa = QA(
            question=question,
            # On pourrait remplir answer avec le tldr
            # (avec article[QuestionAndTldrColumns.tldr]), mais on les laisse
            # tous vides et on les remplit tous un peu plus loin. L'idée étant que pour
            # les nouveaux articles (incorporés car répondant à une question qui était
            # près de l'une des questions des articles donnés en paramètre), il faudra
            # aller faire une requette sql. Dont on traite l'ensemble des tldr (qui feront
            # office de réponse aux questions) un peu plus tard dans le code.
            answer="",  # article[QuestionAndTldrColumns.tldr] aussi possible, cf dessus
            paper_id=paper_id,
            score=cossim_tldr_question,
        )
        # q_and_a is added later in the code not to fetch faiss for unused questions
        all_top_questions[paper_id] = TopQuestions(best_qa=best_qa, q_and_a=[])

    return all_top_questions

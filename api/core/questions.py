from typing import Dict, List, Tuple

from api.core.containers import Paper, s2orcId
from api.memory.faiss import call_question_faiss
from api.memory.sql.questions.questions import add_missing_entries, fetch_questions
from api.memory.sql.questions.utils_questions import (
    add_related_questions_and_answers,
    clean_hs_and_clusterize_questions,
)
from api.specs import THRESHOLD_FOR_OTHER_ANSWERS


def create_questions(best_articles: Dict[s2orcId, Paper], user_query: str):
    n_questions = 100
    score_and_papers: List[Tuple[float, Paper]] = []

    for paper in best_articles.values():
        score = paper.general_score
        score_and_papers.append((score, paper))

    score_and_papers = sorted(score_and_papers, key=lambda pair: pair[0])[::-1]
    if len(score_and_papers) > n_questions:
        score_and_papers = score_and_papers[:n_questions]

    papers_for_questions = [paper for _, paper in score_and_papers]

    related_questionning = call_question_faiss(question=user_query, k=2)
    perfect_questions_ids = [
        int(q["paper_id"]) for q in related_questionning if q["score"] > 0.9
    ]

    questions_uncleaned = fetch_questions(
        ids=perfect_questions_ids + [paper.s2orc_id for paper in papers_for_questions]
    )

    # remove question not containing a question mark
    questions_uncleaned = {
        key: value
        for key, value in questions_uncleaned.items()
        if "?" in value.best_qa.question
    }

    questions_cleaned = clean_hs_and_clusterize_questions(
        questions_uncleaned, user_query=user_query
    )

    add_related_questions_and_answers(questions_cleaned)

    add_missing_entries(questions_cleaned)

    # We delete duplicates in the q_and_a
    # Python 3.7+ Dictionary iteration order is guaranteed to be in order of insertion.
    for id_i, top_question in questions_cleaned.items():
        questions_cleaned[id_i].q_and_a = list(
            {qa.paper_id: qa for qa in top_question.q_and_a}.values()
        )

    questions = []

    for paper_id in questions_cleaned.keys():
        top_questions = questions_cleaned[paper_id]
        answer = top_questions.best_qa.to_dict_front()

        other_answers = [
            qa.to_dict_front()
            for qa in top_questions.q_and_a
            if qa.score > THRESHOLD_FOR_OTHER_ANSWERS and paper_id != qa.paper_id
        ]

        questions.append(
            {
                "question": top_questions.best_qa.question,
                "answers": [answer] + other_answers,
            }
        )

    return questions

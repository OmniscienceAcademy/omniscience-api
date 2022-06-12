from copy import copy
from typing import Dict, List

import numpy as np

from api.memory.faiss import call_cosine_similarity_api, call_question_faiss
from api.memory.sql.questions.questions import QA, TopQuestions
from api.specs import (
    MIN_COS_SIM_QUESTION_QUERY,
    MIN_SCORE_FOR_ARTICLES_ANSWERING_RELATED_QUESTIONS,
    N_FETCHED_ARTICLES_PER_QUESTION,
    THRESHOLD_FOR_QUESTIONS_CLUSTERING,
)


def clusterize_questions(
    questions_to_clusterize: Dict[int, TopQuestions], gramm_matrix_questions
) -> Dict[int, TopQuestions]:
    """Clusterize the remaining questions"""
    list_questions_clusterized = []
    surjection_similar: Dict[int, List[int]] = {}
    for i, (id_i, top_question_i) in enumerate(questions_to_clusterize.items()):
        surjection_similar[id_i] = []
        for j, (id_j, top_question_j) in list(
            enumerate(questions_to_clusterize.items())
        )[i + 1 :]:
            if gramm_matrix_questions[i][j] > THRESHOLD_FOR_QUESTIONS_CLUSTERING:
                list_questions_clusterized.append(id_j)
                surjection_similar[id_i].append(id_j)

    questions_clusterized: Dict[int, TopQuestions] = {}
    for id_i, keys_j in surjection_similar.items():
        if id_i not in list_questions_clusterized:
            questions_clusterized[id_i] = questions_to_clusterize[id_i]
            for id_j in keys_j:

                qa = QA(
                    question=questions_to_clusterize[id_j].best_qa.question,
                    answer=questions_to_clusterize[id_j].best_qa.answer,
                    paper_id=id_j,
                    score=1,
                )
                q_and_a = (
                    [qa]
                    + questions_to_clusterize[id_i].q_and_a
                    + questions_to_clusterize[id_j].q_and_a
                )
                questions_clusterized[id_i].q_and_a = q_and_a

    return questions_clusterized


def remove_invalid_questions(
    questions_uncleaned: Dict[int, TopQuestions], cos_sim_questions_query
) -> Dict[int, TopQuestions]:
    assert len(questions_uncleaned) == len(cos_sim_questions_query)
    indices_invalid_question = np.where(
        np.array(cos_sim_questions_query) < MIN_COS_SIM_QUESTION_QUERY
    )[0]

    # Remove the invalid questions ######
    questions_cleaned = {}
    for i, (id_i, top_questions) in enumerate(questions_uncleaned.items()):
        if i not in indices_invalid_question.tolist():
            questions_cleaned[id_i] = top_questions
    return questions_cleaned


def sort_questions(
    questions_uncleaned: Dict[int, TopQuestions],
    cos_sim_questions_query,
    questions_clusterized: Dict[int, TopQuestions],
) -> Dict[int, TopQuestions]:
    questions_sorted_ids = sorted(
        questions_clusterized,
        key=lambda paper_id: cos_sim_questions_query[
            list(questions_uncleaned.keys()).index(paper_id)
        ],
        reverse=True,
    )
    questions_sorted = {
        id_i: questions_clusterized[id_i] for id_i in questions_sorted_ids
    }

    return questions_sorted


def clean_hs_and_clusterize_questions(
    questions_uncleaned: Dict[int, TopQuestions], user_query: str
) -> Dict[int, TopQuestions]:
    """Clean questions hors sujets and clusterize them"""
    main_questions = [
        top_question.best_qa.question for top_question in questions_uncleaned.values()
    ]

    cos_sim_questions_query, gramm_matrix_questions = call_cosine_similarity_api(
        sentences=main_questions, user_query=user_query, compute_gramm=True
    )

    valid_questions = remove_invalid_questions(
        questions_uncleaned, cos_sim_questions_query
    )

    questions_clusterized = clusterize_questions(
        valid_questions, gramm_matrix_questions
    )

    questions_sorted = sort_questions(
        questions_uncleaned, cos_sim_questions_query, questions_clusterized
    )

    return questions_sorted


def add_related_questions_and_answers(
    all_top_questions: Dict[int, TopQuestions]
) -> None:
    # fetch FAISS-questions to add the field `q_and_a` to every TopQuestions
    # of `all_top_questions`, used to access the articles answering a question related
    # to `best_qa`
    for paper_id, top_questions in all_top_questions.items():
        best_question = top_questions.best_qa.question

        # related questions, and their corresponding article
        related_questionning = call_question_faiss(  # 95 %
            best_question, N_FETCHED_ARTICLES_PER_QUESTION
        )
        q_and_a: List[QA] = []
        for questioning in related_questionning:
            score = questioning["score"]
            if score < MIN_SCORE_FOR_ARTICLES_ANSWERING_RELATED_QUESTIONS:
                continue
            sub_question = questioning["question"]
            sub_paper_id = questioning["paper_id"]
            q_and_a.append(
                QA(
                    question=sub_question,
                    answer="",  # cf la remarque ci dessus
                    paper_id=sub_paper_id,
                    score=0,  # on devra la calculer plus tard
                )
            )
        # si la question principale n'est pas dans la liste des questions-réponses
        # secondaires, on l'ajoute TODO est ce vraiment necessaire ? -> depend de FAISS
        if paper_id not in [qa.paper_id for qa in q_and_a]:
            q_and_a.append(copy(top_questions.best_qa))
        all_top_questions[paper_id].q_and_a = q_and_a

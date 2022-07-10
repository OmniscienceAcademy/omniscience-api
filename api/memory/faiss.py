import json
from typing import Any, Dict, List, Literal, Optional, Tuple

import requests
from spacy.lang.en import English

from api.core.containers import YearRange, prePaper2, s2orcId
from api.specs import BACKEND_URL


def call_cosine_similarity_api(
    user_query: str, sentences: List[str], compute_gramm: bool = False
):
    """Returns either a List[float] or a Tuple[List[float], List[List[float]]]"""
    data = {"user_query": user_query, "sentences": sentences}
    # TODO: put also that in new backend
    url = BACKEND_URL + "/api/compute_cosine_similarity/"

    if compute_gramm:
        if sentences:
            data["compute_gramm"] = True  # type: ignore
            response = requests.post(url, json.dumps(data))
            response_dict = json.loads(response.text)
            return response_dict["similarities"], response_dict["gramm_matrix"]
        else:
            return [], []
    else:
        if sentences:
            data["compute_gramm"] = False  # type: ignore
            response = requests.post(url, json.dumps(data))
            response_dict = json.loads(response.text)
            return response_dict["similarities"]
        else:
            return []


def util_call_api(
    fonction: Literal["abstract", "title", "question"],
    user_query: str,
    retriever_q: int,
    correct_cossim: Optional[int],
    yearRange: Optional[YearRange] = None,
):
    assert retriever_q > 1
    data = {
        "user_query": user_query,
        "retriever_q": retriever_q,
        "correct_cossim": correct_cossim,
        "startYear": yearRange["startYear"] if yearRange else None,
        "endYear": yearRange["endYear"] if yearRange else None,
    }
    if correct_cossim == 1 and fonction == "abstract":
        raise ValueError("abstract is not available with correct_cossim=1")
    url = BACKEND_URL + f"/{fonction}_query/"
    response = requests.post(url, data=json.dumps(data))
    res = json.loads(response.text)
    return res


def call_title_faiss(
    text: str, k: int, yearRange: YearRange
) -> Tuple[Dict[s2orcId, float], YearRange]:
    # {text} can be a user query, or the title of an article, to find related articles
    res_ = util_call_api("title", text, k, correct_cossim=None, yearRange=yearRange)
    res = res_["query"]["documents"]

    ids_and_scores: Dict[s2orcId, float] = {}
    for dic in res:
        s2orc_id = int(dic["meta"]["paper_id"])
        faiss_score = dic["score"]
        # year = int(dic["meta"]["year"]) if dic["meta"]["year"] else None,
        ids_and_scores[s2orc_id] = faiss_score

    extrYearRange = YearRange(
        startYear=int(res_["min_year"]), endYear=int(res_["max_year"])
    )

    return ids_and_scores, extrYearRange


def call_question_faiss(question: str, k: int = 100) -> List[Dict[str, Any]]:
    res_ = util_call_api("question", question, k, correct_cossim=None)
    results = res_["query"]["documents"]
    related_questioning = []
    for res in results:
        questioning = {
            "question": res["content"],
            "paper_id": res["meta"]["paper_id"],
            "score": res["score"],
        }
        related_questioning.append(questioning)
    return related_questioning


nlp_sentencizer = English()
nlp_sentencizer.add_pipe("sentencizer")


def put_in_bold_answer(full_context: str, answer: str):
    """Put the answer in bold. The answer include full sentences."""

    answer = answer.strip(" ")
    assert answer in full_context

    doc = nlp_sentencizer(full_context)
    full_context_sentences = doc.sents

    doc = nlp_sentencizer(answer)
    answer_sentences = doc.sents

    bools = []
    for sent in enumerate(full_context_sentences):
        context_in = any(
            str(chunk_answer) in str(sent) for chunk_answer in answer_sentences
        )
        bools.append(context_in)

    first_sentence_idx = 0
    last_sentence_idx = len(bools) - 1
    if True in bools:
        first_sentence_idx = bools.index(True)
        last_sentence_idx = len(bools) - 1 - bools[::-1].index(True)

    doc = nlp_sentencizer(full_context)
    full_context_sentences = doc.sents
    partial_contexts = [
        str(sent)
        for i, sent in enumerate(full_context_sentences)
        if i in list(range(first_sentence_idx, last_sentence_idx + 1))
    ]
    partial_context = " ".join(partial_contexts)
    return partial_context.replace(answer, "<b>" + answer + "</b>")


def call_abstract_faiss(question: str) -> Dict[str, Any]:

    questions_words = ["what", "who", "when", "where", "why", "how"]
    is_question = any(word in question.lower() for word in questions_words)
    if not is_question:
        return {}
    json_res = util_call_api(
        fonction="abstract", user_query=question, retriever_q=2, correct_cossim=0
    )
    answers = json_res["query"]["answers"]
    if not answers:
        return {}
    first_answer = answers[0]

    no_ans_gap = json_res["query"]["no_ans_gap"]
    score = first_answer["score"]
    paper_id = int(first_answer["meta"]["paper_id"])
    document_id = first_answer["document_id"]
    answer = first_answer["answer"]
    context = first_answer["context"]
    full_context = [
        doc["content"]
        for doc in json_res["query"]["documents"]
        if doc["id"] == document_id
    ][0]

    assert answer in context
    # the context with the answer in bold

    # final_text = full_context.replace(answer, "<b>" + answer + "</b>")

    return {
        "score": score,
        "paper_id": paper_id,
        "answer": put_in_bold_answer(full_context, answer),
        "no_ans_gap": no_ans_gap,  # currently unused
    }


def get_faiss_scores(
    papers: Dict[s2orcId, prePaper2], user_query: str
) -> Dict[s2orcId, float]:
    sentences = [paper.title for paper in papers.values()]
    cosine_similarities = call_cosine_similarity_api(user_query, sentences)
    faiss_scores: Dict[s2orcId, float] = {}
    for i, s2orc_id in enumerate(papers.keys()):
        faiss_scores[s2orc_id] = float(cosine_similarities[i])  # type:ignore
    return faiss_scores

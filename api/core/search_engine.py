import heapq
from typing import Dict, Iterable, Set, Tuple

import numpy as np

from api.core.containers import Paper, YearRange, s2orcId
from api.core.score import add_general_scores
from api.core.tags import add_many_tags, add_tags_to_final_papers
from api.memory.elasticsearch import search_titles_elasticsearch
from api.memory.faiss import call_title_faiss, get_faiss_scores
from api.memory.sql.s2orc.interract_sql import fetch_papers
from api.specs import (
    BONUS_SEMINAL,
    MIN_N_ARTICLES_CITING_SEMINAL,
    N_ARTICLES_FAISS,
    N_RETURNED_ARTICLES,
    RANGE_MOST_CITED_ARTICLES,
)


def merge_faiss_elasticsearch_scores(
    faiss_scores: Dict[s2orcId, float], elasticsearch_scores: Dict[s2orcId, float]
) -> Dict[s2orcId, float]:
    """Faiss is prioritary but if not in faiss, we use elasticsearch score"""
    merged_scores = elasticsearch_scores.copy()
    for id, score in faiss_scores.items():
        merged_scores[id] = score

    # Add print to debug
    return merged_scores


def search_papers(
    user_query: str, yearRange: YearRange
) -> Tuple[Dict[s2orcId, Paper], YearRange]:
    # [Pas important] Actuellement on fetch faiss sur 120, puis on fetch la bdd
    # sur 120, puis on calcule les general_score et on renvoie les 30 meilleurs.
    # On pourrait faire deux requettes sql,n d'abord fetch sur 120 year + nb in
    # citations, calculer avec ca (+ avec le faiss score) le general score,
    # et ne fetch la bdd sur toutes les colonnes uniquement pour les 60 meilleurs

    ids_and_scores_faiss, extrYearRange = call_title_faiss(
        user_query, k=N_ARTICLES_FAISS, yearRange=yearRange
    )

    ids_and_scores_elastic = search_titles_elasticsearch(user_query)
    ids_and_scores = merge_faiss_elasticsearch_scores(
        faiss_scores=ids_and_scores_faiss, elasticsearch_scores=ids_and_scores_elastic
    )

    _papers = fetch_papers(list(ids_and_scores.keys()))
    papers = add_general_scores(_papers, ids_and_scores)
    best_papers = get_papers_with_highest_general_score(papers, N_RETURNED_ARTICLES)

    incorporate_seminal_papers(papers, user_query)
    best_papers = get_papers_with_highest_general_score(papers, N_RETURNED_ARTICLES)

    add_tags_to_final_papers(best_papers)
    return best_papers, extrYearRange


def get_papers_with_highest_general_score(
    papers: Dict[s2orcId, Paper], n: int
) -> Dict[s2orcId, Paper]:
    ids = list(papers.keys())
    sorted_ids = sorted(ids, key=lambda id: papers[id].general_score, reverse=True)
    best_ids = sorted_ids[:n]
    best_papers = {s2orc_id: papers[s2orc_id] for s2orc_id in best_ids}
    return best_papers


def incorporate_seminal_papers(papers: Dict[s2orcId, Paper], user_query: str) -> None:
    # the seminal articles are those which are the most cited by our papers
    n_citations: Dict[int, int] = {}

    for paper in papers.values():
        for id in paper.outbound_citations:
            if id not in n_citations:
                n_citations[id] = 1
            else:
                n_citations[id] += 1

    seminal_ids = get_best_keys(
        n_citations, RANGE_MOST_CITED_ARTICLES, min_v=MIN_N_ARTICLES_CITING_SEMINAL
    )

    incorporate_papers_from_ids(
        papers, seminal_ids, user_query, bonus_score=BONUS_SEMINAL
    )

    add_many_tags(papers, seminal_ids, tag="Seminal", color="#A3BAE3")


def incorporate_papers_from_ids(
    papers: Dict[s2orcId, Paper],
    new_ids: Iterable[int],
    user_query: str,
    bonus_score: float = 0,
) -> None:
    new_ids = [id for id in new_ids if id not in papers]

    _new_papers = fetch_papers(new_ids)
    faiss_scores = get_faiss_scores(_new_papers, user_query)

    faiss_scores = {
        id: score + bonus_score
        for id, score in faiss_scores.items()
        if score is not None
    }

    new_papers = add_general_scores(_new_papers, faiss_scores)

    assert not set(new_papers.keys()).intersection(set(papers.keys()))
    papers.update(new_papers)


def get_best_keys(my_dict: Dict[int, int], n_keys: int, min_v: float) -> Set[int]:
    """Returns the top {n_keys} keys of {my_dict} that have the maximum values.
    Example:
    - my_dict = {1112: 4, 222224: 5, 333335: 2, 444454: 5555587: 6}
    - n_keys = 2
    returns: {4, 1}
    """
    my_dict = {k: v for k, v in my_dict.items() if v >= min_v}

    if n_keys >= len(my_dict):
        return set(my_dict.keys())

    my_items = list(my_dict.items())
    values = [my_items[k][1] for k in range(len(my_items))]

    best_indexes = heapq.nlargest(n_keys, range(len(values)), np.array(values).take)
    best_keys = [my_items[u][0] for u in best_indexes]

    assert len(best_keys) == n_keys
    return set(best_keys)

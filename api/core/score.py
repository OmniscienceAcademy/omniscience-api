from math import exp
from typing import Dict

import numpy as np

from api.core.containers import Paper, prePaper2, s2orcId


def sigmoid(x):
    return 1 / (1 + exp(-x))


def get_general_score(faiss_score: float, nb_citations: int, year: int) -> float:
    """+2 decenies == + *10 citations == 0.04"""
    general_score = faiss_score
    general_score += 0.05 * np.log10(nb_citations + 1)
    general_score += 0.05 if nb_citations > 1 else 0
    general_score += 0.002 * min(max(year - 2000, 0), 20) if year else 0
    general_score = sigmoid(10 * general_score - 7)
    # Rajouter impact factor ici
    return general_score


def add_general_scores(
    papers: Dict[s2orcId, prePaper2], faiss_scores: Dict[s2orcId, float]
) -> Dict[s2orcId, Paper]:
    new_papers: Dict[s2orcId, Paper] = {}
    for s2orc_id, paper in papers.items():
        general_score = get_general_score(
            faiss_score=faiss_scores[s2orc_id],
            nb_citations=paper.nb_inbound_citations,
            year=paper.year,
        )
        new_papers[s2orc_id] = Paper(paper=paper, general_score=general_score)

    return new_papers

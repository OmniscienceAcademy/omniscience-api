from typing import Dict, List, Tuple

from api.core.containers import Paper, s2orcId


def create_graph(papers: Dict[s2orcId, Paper]):

    nodes_degres_0 = [paper.s2orc_id for paper in papers.values()]
    edges: List[Tuple[s2orcId, s2orcId]] = []
    for paper in papers.values():
        # TODO REPRENDRE remttre bien
        # inter citations
        # todo properly (pas urgent)
        id = paper.s2orc_id
        edges = edges + [
            (id, id_cited)
            for id_cited in paper.outbound_citations
            if id_cited in nodes_degres_0
        ]

        # seminal papers

        # Followup papers

    return {"nodes": nodes_degres_0, "edges": edges}

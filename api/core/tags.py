from typing import Dict, Iterable

import pandas as pd

from api.core.containers import Paper, s2orcId
from api.memory.sql.mag.mag_queries import (
    fetch_doctypes_by_ids,
    fetch_fields_of_study_by_ids,
    fetch_wiki_fields_of_studies,
    select_mag_id,
)


def get_tag_priority(tag: str) -> int:
    # the highest the tag priority is, the highest the returned value is
    # (tags with a hight priority are displayed first in the front)
    if tag == "Seminal":
        return 2
    return 1


def add_tag(paper: Paper, tag: str, color: str) -> None:
    for i in range(len(paper.tags)):
        if get_tag_priority(tag) > get_tag_priority(paper.tags[i]["tag"]):
            paper.tags.insert(i, {"tag": tag, "color": color})
            return
    paper.tags.append({"tag": tag, "color": color})


def add_many_tags(
    papers: Dict[s2orcId, Paper], ids: Iterable[int], tag: str, color: str
) -> None:
    for paper_id, paper in papers.items():
        if paper_id in ids:
            add_tag(paper, tag, color)


def add_fields_of_studies_tag(paper: Paper) -> None:
    mag_ids = paper.mag_ids
    df_magId_field = fetch_fields_of_study_by_ids([mag_ids])

    fields_of_study = df_magId_field.loc[
        df_magId_field["mag_id"] == select_mag_id(mag_ids), "fieldofstudy"
    ].values.tolist()  # type: ignore
    for field_of_study in fields_of_study:
        add_tag(paper, field_of_study, "white")


def get_wiki_url(
    df_magId_field: pd.DataFrame, best_papers: Dict[s2orcId, Paper], query: str
) -> str:
    # si la query est contenue dans des df_magId_field
    idxs = []
    for index, row in df_magId_field.iterrows():
        if (
            isinstance(row["fieldofstudy"], str)
            and row["fieldofstudy"].lower() in query.lower()
        ):  # type:ignore
            idxs.append(index)
    if idxs:
        df_magId_field = df_magId_field.loc[idxs]
    else:
        return ""

    # top 5 fieldofstudyid
    fiel_of_study_ids = df_magId_field.loc[:, "fieldofstudyid"].tolist()  # type: ignore
    # on eneleve les duplicats des fields of studies
    fiel_of_study_ids = list(set(fiel_of_study_ids))
    # on fetch les url de wikipédia associés
    wiki_fields_of_study = fetch_wiki_fields_of_studies(fiel_of_study_ids)

    # la liste des couples (general score, paper)
    scores_and_papers = [(paper.general_score, paper) for paper in best_papers.values()]
    # on trie par ordre croissant de 'general score', correspondant a l'element a
    # l'indice 0 de chaque tuple
    sorted_scores_and_papers = sorted(
        scores_and_papers, key=lambda x: x[0], reverse=True
    )
    # on prend le wiki du papier avec le plus gros score qui a une URL valide
    for score_and_paper in sorted_scores_and_papers:
        paper = score_and_paper[1]
        mag_id = select_mag_id(paper.mag_ids)
        if mag_id not in df_magId_field["mag_id"].tolist():
            continue
        field_of_study_id = df_magId_field.loc[df_magId_field["mag_id"] == mag_id][
            "fieldofstudyid"
        ].iloc[0]
        if field_of_study_id not in wiki_fields_of_study:
            continue
        wiki_url = wiki_fields_of_study[field_of_study_id]
        return wiki_url

    return ""


def add_tags_to_final_papers(papers: Dict[s2orcId, Paper]) -> None:
    # Add doc type to the list
    mappping_magid_to_doctype = fetch_doctypes_by_ids(
        mag_ids=[paper.mag_ids for paper in papers.values()]
    )

    ADD_DOC_TYPE_TO_LIST_RES = True
    if ADD_DOC_TYPE_TO_LIST_RES:
        for paper in papers.values():
            mag_id = select_mag_id(paper.mag_ids)
            if mag_id is not None and mag_id in mappping_magid_to_doctype:
                for field in mappping_magid_to_doctype[
                    str(mag_id)
                ]:  # TODO reprendre ici
                    if field:
                        add_tag(paper, field, "rose")

import io
import sqlite3
from typing import Dict, Iterable, List, Optional, Union

import numpy as np

import api.memory.sql.omni_config_sql as omni_config_sql
from api.core.containers import prePaper0, prePaper1, prePaper2, s2orcId
from api.memory.sql.clean_fetching import clean_article
from api.memory.sql.questions.questions import fetch_questions
from api.memory.sql.s2orc.columns import ArticleS2ORC, QuestionAndTldr
from api.memory.sql.s2orc.interract_sql_aux import (
    add_mag_columns,
    clean_outbound_citations,
)

# ----------------------------------------------------------------------------
# we will create a new data type to store numpy arrays in sqlite


def adapt_numpy_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())


def convert_numpy_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


# Converts np.array to TEXT when inserting
sqlite3.register_adapter(np.ndarray, adapt_numpy_array)
# Converts TEXT to np.array when selecting
sqlite3.register_converter("array", convert_numpy_array)

# ---------------------------------------------------------------------------


def to_str(o: Union[None, str]) -> str:
    # convert None to empty string
    if o is None:
        return ""
    else:
        return o


def to_int(o: Union[None, int]) -> int:
    # convert None to empty string
    if o is None:
        return 0
    else:
        return o


def to_float(o: Union[None, float]) -> float:
    # convert None to empty string
    if o is None:
        return 0.0
    else:
        return o


def fetch_papers(
    ids: List[int],
    use_only_python_lists=False,
    user_query: Optional[str] = None,
    # n_most_cited: int = 50,
    return_questions: bool = False,
) -> Dict[s2orcId, prePaper2]:

    if not ids:
        return {}

    columns = [
        # ArticleS2ORC
        ArticleS2ORC.paper_id,
        ArticleS2ORC.mag_id,
        ArticleS2ORC.title,
        ArticleS2ORC.abstract,
        ArticleS2ORC.s2_url,
        ArticleS2ORC.inbound_citations,
        ArticleS2ORC.outbound_citations,
        ArticleS2ORC.nb_inbound_citations,
        ArticleS2ORC.nb_outbound_citations,
        ArticleS2ORC.year,
        ArticleS2ORC.journal,
        ArticleS2ORC.venue,
        # QuestionAndTldr,
        QuestionAndTldr.tldr,
        QuestionAndTldr.question,
        QuestionAndTldr.cossim_tldr_question,
    ]

    query = (
        omni_config_sql.session.query(*columns)
        .outerjoin(QuestionAndTldr, ArticleS2ORC.paper_id == QuestionAndTldr.paper_id)
        .filter(ArticleS2ORC.paper_id.in_(ids))
    )

    query = query.all()

    papers0: Dict[s2orcId, prePaper0] = {}

    for row in query:
        s2orc_id = row[0]
        papers0[s2orc_id] = prePaper0(
            s2orc_id=s2orc_id,
            mag_ids=row[1],
            title=to_str(row[2]),
            abstract=to_str(row[3]),
            s2_url=to_str(row[4]),
            inbound_citations=row[5],
            outbound_citations=row[6],
            nb_inbound_citations=to_int(row[7]),
            nb_outbound_citations=to_int(row[8]),
            year=to_int(row[9]),
            journal=to_str(row[10]),
            venue=to_str(row[11]),
            tldr=to_str(row[12]),
            question=to_str(row[13]),
            cossim_tldr_question=to_float(row[14]),
            tags=[],
        )

    clean_outbound_citations(papers=papers0)

    papers1: Dict[s2orcId, prePaper1] = add_mag_columns(papers0)

    # cf TODO 412548574963195826985
    # (peu prioritaire, en gros comprendre dans quels
    # moments certains ids ne sont pas dans la bdd)
    ids_to_delete = [id for id in papers1.keys() if not papers1[id]]
    for id in ids_to_delete:
        del papers1[id]

    for paper in papers1.values():
        clean_article(
            paper=paper,
            use_only_python_lists=use_only_python_lists,
            user_query=user_query,
        )

    papers2 = add_questions(return_questions=return_questions, papers=papers1)

    return papers2


def add_questions(
    return_questions: bool, papers: Dict[s2orcId, prePaper1]
) -> Dict[s2orcId, prePaper2]:
    if return_questions:
        dict_questions = fetch_questions(ids=list(papers.keys()))
    else:
        dict_questions = {}

    new_papers: Dict[s2orcId, prePaper2] = {}
    for s2orc_id, paper1 in papers.items():
        if s2orc_id in dict_questions:
            top_questions = dict_questions[s2orc_id]
            qa_dict = top_questions.to_dict()
        else:
            qa_dict = {}
        new_papers[s2orc_id] = prePaper2(paper1, qa_dict=qa_dict)
    return new_papers


def get_most_cited_ids(ids: Iterable[int], N=10) -> List[int]:
    # Get the id of the N most cited articles.
    query = omni_config_sql.session.query(ArticleS2ORC.paper_id).filter(
        ArticleS2ORC.paper_id.in_(ids)
    )
    query = query.order_by(ArticleS2ORC.nb_inbound_citations.desc())
    query = query.limit(N)
    most_cited_ids: List[s2orcId] = [row[0] for row in query]

    return most_cited_ids

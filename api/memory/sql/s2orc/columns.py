# type: ignore
"""The columns of our sql database."""
from typing import List

from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import ARRAY

from api.memory.sql.omni_config_sql import (
    TABLE_NAME_ARTICLES,
    TABLE_NAME_QUESTION_AND_TLDR,
    get_engine_articles,
)

article_engine = get_engine_articles()
articleBase = declarative_base()


class ArticleS2ORC(articleBase):
    __tablename__ = TABLE_NAME_ARTICLES

    paper_id = Column(Integer, primary_key=True)
    title = Column(String)
    abstract = Column(String)
    year = Column(Integer)
    arxiv_id = Column(String)
    acl_id = Column(String)
    pmc_id = Column(String)
    pubmed_id = Column(String)
    doi = Column(String)
    venue = Column(String)
    journal = Column(String)
    mag_id = Column(ARRAY(Integer))
    # mag_field_of_study = Column(String)
    outbound_citations = Column(ARRAY(Integer))
    inbound_citations = Column(ARRAY(Integer))
    has_outbound_citations = Column(Boolean)
    has_inbound_citations = Column(Boolean)
    has_pdf_parse = Column(Boolean)
    s2_url = Column(String)
    has_pdf_body_text = Column(Boolean)
    has_pdf_parsed_abstract = Column(Boolean)
    has_pdf_parsed_body_text = Column(Boolean)
    has_pdf_parsed_bib_entries = Column(Boolean)
    has_pdf_parsed_ref_entries = Column(Boolean)
    nb_outbound_citations = Column(Integer)
    nb_inbound_citations = Column(Integer)

    def get_list_of_columns_names(self) -> List[str]:
        return [column.name for column in self.__table__.columns]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<Article(id='{self.paper_id}', title='{self.title}')>"


question_and_tldr_engine = get_engine_articles()
questionAndTldrBase = declarative_base()


class QuestionAndTldr(questionAndTldrBase):
    __tablename__ = TABLE_NAME_QUESTION_AND_TLDR

    paper_id = Column(Integer, primary_key=True)
    question = Column(String)
    tldr = Column(String)
    cossim_title_abstract = Column(Float)
    cossim_title_tldr = Column(Float)
    cossim_title_question = Column(Float)
    cossim_abstract_tldr = Column(Float)
    cossim_abstract_question = Column(Float)
    cossim_tldr_question = Column(Float)
    n_word_question = Column(Integer)
    score_question = Column(Float)

    def get_list_of_columns_names(self) -> List[str]:
        return [column.name for column in self.__table__.columns]

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return (
            f"<QuestionAndTldr(paper_id='{self.paper_id}', "
            + f"question='{self.question}', "
            + f"tldr='{self.tldr}')>"
        )

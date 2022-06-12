from typing import Any, Dict, List, TypedDict

s2orcId = int
magId = int
magAuthorId = int


class prePaper0:
    def __init__(
        self,
        s2orc_id: s2orcId,
        mag_ids: List[magId],
        title: str,
        abstract: str,
        year: int,
        journal: str,
        venue: str,
        outbound_citations: List[s2orcId],
        inbound_citations: List[s2orcId],
        s2_url: str,
        nb_outbound_citations: int,
        nb_inbound_citations: int,
        question: str,
        tldr: str,
        cossim_tldr_question: float,
        tags: List[Dict[str, str]],  # TODO creer classe Tag
    ) -> None:
        self.s2orc_id = s2orc_id
        self.mag_ids = mag_ids
        self.title = title
        self.abstract = abstract
        self.year = year
        self.journal = journal
        self.venue = venue
        self.outbound_citations = outbound_citations
        self.inbound_citations = inbound_citations
        self.s2_url = s2_url
        self.nb_outbound_citations = nb_outbound_citations
        self.nb_inbound_citations = nb_inbound_citations
        self.question = question
        self.tldr = tldr
        self.cossim_tldr_question = cossim_tldr_question
        self.tags = tags

    def __str__(self) -> str:
        # for debug only
        res = "[Paper]\n"

        for key, value in self.__dict__.items():
            value_str = str(value)
            if len(value_str) > 20:
                value_str = value_str[:20] + "..."
            res += "\t" + key + ": " + value_str + "\n"
        return res


class prePaper1(prePaper0):
    def __init__(
        self,
        paper: prePaper0,
        paper_url: str,
        mag_authors: Dict[magId, str],
        github_urls: List[str],
    ) -> None:
        self.__dict__.update(paper.__dict__)
        self.paper_url = paper_url
        self.mag_authors = mag_authors
        self.github_urls = github_urls


class prePaper2(prePaper1):
    # TODO meilleur typage pour qa_dict
    def __init__(self, paper: prePaper1, qa_dict: Dict[str, Any]) -> None:
        self.__dict__.update(paper.__dict__)
        self.qa_dict = qa_dict


class Paper(prePaper2):
    def __init__(self, paper: prePaper2, general_score: float) -> None:
        self.__dict__.update(paper.__dict__)
        self.general_score = general_score


class YearRange(TypedDict):
    startYear: int
    endYear: int

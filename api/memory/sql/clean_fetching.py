import re
from typing import Optional

import numpy as np

from api.core.containers import prePaper1
from api.services.spacy import put_in_bold_matching_words


def clean_tldr(tldr: str) -> str:
    if not tldr:
        return ""

    # Avoid duplications
    # "Charbel is a crack. Charbel is a crack." -> "Charbel is a crack."
    middle = len(tldr) // 2
    if tldr[:middle] == tldr[middle + 1 :]:
        tldr = tldr[:middle]

    if "ElaborateElaborate" in tldr:
        return ""

    return tldr


def clean_abstract(abstract: str) -> str:
    """Remove the word 'abstrac' from the abstract"""
    if not abstract:
        return ""

    if "abstract" in abstract[:30].lower():
        # seek position of the word abstract in the 30 first characters
        pos = abstract[:30].lower().find("abstract")
        # remove the word abstract
        abstract = abstract[pos + len("abstract") :]

    return abstract


taboo = [
    "Paper",
    "Article",
    "manuscript",
    "act",
    "exercise",
    "Study",
    "book",
    "project",
    "case",
    "content",
    "course",
    "conference",
    "invention",
    "phrase",
    "chapter",
    "research",
    "thesis",
    "essay",
    # # # # # # # # "studies", Ce serait tricher. L'étude de faisabilité montre que mettre des taboo comme ça enleve plein de bons articles. # noqa
    # # # # # # # # "Nobel",
    "model",
    # "publication",
    "dissertation",
    # "report",
    # "note", # contained in bigger words
    # "essays",
    # "assessment",
    # "work",
    # "RESUME",
    # "name",
    # "reform",
    # "survey",
    # "table",
    # "ii",
    # "text",
    # "do",
    # "deal",
    # "section",
    # "comment",
    # "workshop",
    # "program",
    # "meeting",
    # "read",
    # "brief",
    # "editorial",
    # "experiment",
    # "agreement",
    # "author",
    # "authors",
    # "symposium",
    # "lecture",
    # "amendment",
    # "decision",
    # "contribution",
    # "investigation",
    # "evaluation",
    # "abstract",
    # "monograph",
    # "discussion",
    # "seminar",
    # "model",
    # "debate",
    # "argument",
    # "letter",
    # "acknowledgements",
    # "acknowledge",
    # "tag",
    # "v.",
    # "iii",
    # # "What is the?", # ? is a symbol for unknown caracters
    # "What is the difference",
]

# construct a regex to find bad questions and tell if bad questions
taboo = [word.lower() for word in taboo]
regex = "|".join(taboo)
regex = r"(?i)" + regex
regexcompiled = re.compile(regex)


def clean_question(question: str) -> str:
    if not question:
        return ""

    # This list should contain uncased words
    taboo_particular_cases = ["what is the?", "........", "happiness", "happy"]

    lower_question = question.lower()
    if any(word in lower_question for word in taboo_particular_cases):
        return ""

    if regexcompiled.search(lower_question):
        return ""

    return question


def clean_unknown_caracters(paper: prePaper1) -> None:
    # Solving the bug of unknown caracters
    # https://www.omniscienceapi.com:4430/get-article-by-id/f29232da1e563ef67b26cf8965326d4580448cb8/
    paper.title.replace("\ufffd?", " ")
    paper.abstract.replace("\ufffd?", " ")


def clean_article(
    paper: prePaper1, use_only_python_lists=False, user_query: Optional[str] = None
) -> None:

    # replace_none_by_empty_str(paper)

    if use_only_python_lists:
        if type(paper.outbound_citations) == np.ndarray:
            paper.outbound_citations = paper.outbound_citations.tolist()  # type:ignore

    clean_unknown_caracters(paper)

    paper.abstract = clean_abstract(paper.abstract)

    # Putting in bold the query matching words
    # user_query is a non empty string <-> need to apply bold
    if user_query:
        paper.abstract = put_in_bold_matching_words(
            abstract=paper.abstract, user_query=user_query
        )
    paper.tldr = clean_tldr(paper.tldr)
    paper.question = clean_question(paper.question)

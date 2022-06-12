from typing import Dict, List, Set, Tuple, Union

import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector


def fast_pipeline(used_pipes, nlp):
    for pipe_name in nlp.pipe_names:
        if pipe_name not in used_pipes:
            nlp.disable_pipe(pipe_name)


used_pipes = ["tagger", "attribute_ruler", "lemmatizer"]
nlp = spacy.load("en_core_web_sm")  # type: ignore
fast_pipeline(used_pipes, nlp)


nlp_language = spacy.load("en_core_web_sm")  # type: ignore
fast_pipeline([], nlp_language)

nlp_language.add_pipe("sentencizer")

stopwords: Set[str] = spacy.lang.en.stop_words.STOP_WORDS  # type: ignore
stopwords.add(" ")


def get_lang_detector(nlp, name):
    return LanguageDetector()


Language.factory("language_detector", func=get_lang_detector)
nlp_language.add_pipe("language_detector", last=True)


def find_language(text: str) -> Dict[str, Union[str, float]]:
    # returns (for instance): {'language': 'en', 'score': 0.9999960006965927}
    doc = nlp_language(text)
    return doc._.language


def put_in_bold_matching_words(abstract, user_query):
    "Return abstract bolded."
    nlp_user_query = nlp(user_query.lower())
    nlp_abstract = nlp(abstract)

    list_token: List[str] = [str(token) for token in nlp_abstract]
    list_bold = [False for token in nlp_abstract]

    lemmas_query = [
        token_query.lemma_.lower()
        for token_query in nlp_user_query
        if str(token_query) not in stopwords
    ]

    for i, token in enumerate(nlp_abstract):
        if token.lemma_.lower() in lemmas_query:
            list_bold[i] = True

    for i, token in enumerate(list_token):
        if list_bold[i]:
            list_token[i] = "<b>" + token + "</b>"

    # see https://stackoverflow.com/questions/60855976/how-to-reconstruct-original-text-from-spacy-tokens-even-in-cases-with-complicat # noqa
    spaCy_toks = [token + i.whitespace_ for token, i in zip(list_token, nlp_abstract)]
    reconstruct = "".join(spaCy_toks)
    return reconstruct


def get_lemmas(text: str) -> Set[str]:
    # remove stop words
    tokens = nlp(text)
    lemmas = set()
    for token in tokens:
        if token.is_alpha and not token.is_stop:
            lemmas |= {token.lemma_}
    return lemmas


used_pipes = ["parser", "tagger", "attribute_ruler", "tok2vec"]
nlp_parser = spacy.load("en_core_web_sm")  # type: ignore
fast_pipeline(used_pipes, nlp_parser)


def get_nouns(text: str) -> List[str]:
    nouns = []
    tokens = nlp_parser(text)
    for token in tokens.noun_chunks:
        nouns.append(token.text)
    return nouns


def get_nouns_2(text: str) -> List[str]:

    nouns = []
    tokens = nlp_parser(text)
    for token in tokens:
        if token.pos_ == "NOUN" and not token.is_stop and not token.is_punct:
            nouns.append(token.text)
    return nouns


used_pipes = ["parser", "tagger", "attribute_ruler", "tok2vec", "lemmatizer"]
nlp_all = spacy.load("en_core_web_sm")  # type: ignore
fast_pipeline(used_pipes, nlp_all)


def get_nouns_3(text: str) -> Tuple[List[str], Set[str]]:
    nouns = []
    tokens = nlp_all(text)
    for token in tokens.noun_chunks:
        nouns.append(token.text)

    lemmas = set()
    for token in tokens:
        if token.is_alpha and not token.is_stop and not token.is_punct:
            lemmas |= {token.lemma_}

    return nouns, lemmas

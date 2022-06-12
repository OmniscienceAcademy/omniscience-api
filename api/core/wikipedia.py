from typing import Any, Dict

import wikipediaapi

from api.specs import MAX_SIZE_WIKI_SUMMARY


def fetch_wikipedia(wiki_url: str) -> Dict[str, Any]:
    # TODO trouver un moyen de fetch wikipedia via une url
    # (actuellemnt on deduit le titre de l'url et on fetch sur le titre)

    if not wiki_url:
        return {}

    _wiki = wikipediaapi.Wikipedia("en")
    # remove potentiel ending slash
    if wiki_url[-1] == "/":
        wiki_url = wiki_url[:-1]

    # deduce title from url
    title = wiki_url[wiki_url.rfind("/") + 1 :]

    page_py = _wiki.page(title)
    if not page_py.exists or not page_py.summary:
        return {}
    summary = (
        page_py.summary[0:MAX_SIZE_WIKI_SUMMARY]
        if len(page_py.summary) <= MAX_SIZE_WIKI_SUMMARY
        else page_py.summary[:MAX_SIZE_WIKI_SUMMARY] + "..."
    )
    return {"title": page_py.title, "url": wiki_url, "text": summary}

import json
from typing import List

import requests

from api.specs import BACKEND_URL


def _predict_next_word(user_query: str, top_k: int) -> List[str]:
    # user_query = "Why is earth"
    # top_k = 4
    # returns ["beautiful", "burning", "boring", "shaking"] ("beautiful"
    # has the higher score, then "burning", ...)

    data = {"user_query": user_query, "top_k": top_k}
    url = BACKEND_URL + "/predict_next_word/"
    response = requests.post(url, json.dumps(data))
    return json.loads(response.text)["predicted_words"]


def complete_query_with_bert(user_query: str, top_k: int) -> List[str]:
    # TODO maybe ? in case the last character of user_query is not " ", an idea would be
    # to remove the word beeing written, call bert on the previous words, that are all
    # complete and to keep the words predicted by bert that are similar to the word beeing
    # written

    if not user_query:
        return []
    if user_query[-1] != " ":
        user_query += " "
    predicted_words = _predict_next_word(user_query, top_k)
    return [user_query + word for word in predicted_words]

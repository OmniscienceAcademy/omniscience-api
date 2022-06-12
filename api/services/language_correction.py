import json

import requests

from api.specs import BACKEND_URL


def call_language_corrector_api(user_query: str):
    data = {"user_query": user_query}
    url = BACKEND_URL + "/language-corrector/"
    response = requests.post(url, json.dumps(data))
    return json.loads(response.text)["corrected_query"]

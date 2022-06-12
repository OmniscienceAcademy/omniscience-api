import json

import pandas as pd
import requests


def call_backend_title_faiss(user_query, k: int = 10):
    """return dataframe with columns indices and distances"""
    user_query = user_query.replace("?", " ")
    url = (
        f"http://aws.omniscienceapidev.com/faiss_articles_with_infos/{user_query}/{k}/"
    )
    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.DataFrame(data["faiss_articles"])
    return df

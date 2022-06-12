import json
from typing import Dict, Literal

import numpy as np
import pandas as pd
import requests

from api.core.containers import s2orcId
from api.specs import BACKEND_URL


def util_call_api_elasticsearch(
    fonction: Literal["abstract", "title", "question"],
    user_query: str,
    # yearRange: Optional[YearRange] = None,
):
    data = {
        "user_query": user_query,
        # "startYear": yearRange["startYear"] if yearRange else None,
        # "endYear": yearRange["endYear"] if yearRange else None,
    }

    url = BACKEND_URL + f"/{fonction}_query_elasticsearch/"
    response = requests.post(url, data=json.dumps(data))
    res = json.loads(response.text)
    return res


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def search_titles_elasticsearch(user_query: str,) -> Dict[s2orcId, float]:
    """title, paper_id, bm25 score (negative, more negative = bettter)"""
    res = util_call_api_elasticsearch("title", user_query)

    df = pd.DataFrame(res["query"], columns=["elastic_score", "paper_id"])

    df["elastic_score"] = df["elastic_score"].astype(float)
    df["paper_id"] = df["paper_id"].astype(int)

    # convert elasticscores into cosine similarity scores
    df["elastic_score"] = df["elastic_score"] / 14
    df["elastic_score"] = sigmoid(df["elastic_score"])

    # convert into a dict
    return dict(zip(df["paper_id"], df["elastic_score"]))

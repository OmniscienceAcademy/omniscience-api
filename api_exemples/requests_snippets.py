import asyncio
import json
from random import choice
from time import time

import requests
from matplotlib import pyplot as plt
from top_words import top_words

base_url = "http://127.0.0.1:8000/"


def call_get_articles_by_ids():

    ids = [
        60254183,
        2397047,
        155186215,
        59765070,
        64218422,
        21362914,
        62959673,
        14317037,
        60244901,
        62979363,
        64345956,
        155204858,
        210671292,
        17300178,
        58751956,
        60106064,
        63132174,
        46411847,
        36574706,
        18068263,
        10074376,
        60282266,
        35456915,
        17607175,
        64205276,
        22377583,
    ]
    response = requests.post(base_url + "get-articles-by-id/", json={"ids": ids})
    print(json.loads(response.content)["articles"])


def call_get_authors_by_id():
    authors_id = [
        199142497,
        680395887,
        2582258949,
        2641488431,
        2137699977,
        2421676522,
        2694702754,
    ]
    response = requests.post(base_url + "get-authors-by-id/", json={"ids": authors_id})
    print(response.content)
    res = json.loads(response.content)["authors"]
    print(res)


def get_results():
    swipe_session_token = "5f4ac96c60356dcabbf7"
    response = requests.get(
        base_url + f"get-results-swipe/{swipe_session_token}/", json={}
    )
    print(json.loads(response.content))


def get_authors():
    mag_author_ids = [2002927953, 2337230968, 1502687800]
    response = requests.post(
        base_url + "get-authors-by-id/", json={"ids": mag_author_ids}
    )
    print(json.loads(response.content))


async def _send_requests(n_requests, verbose=False):
    front_git_dev_url = "https://aws.omniscienceapidev.com/get-direct-results/"
    loop = asyncio.get_event_loop()
    user_queries = [
        choice(top_words) + " " + choice(top_words) for _ in range(n_requests)
    ]
    urls = [front_git_dev_url + query for query in user_queries]
    futures = [loop.run_in_executor(None, requests.get, url) for url in urls]
    t1 = time()
    responses = [await future for future in futures]
    t2 = time()
    delta = t2 - t1
    if verbose:
        [print(response.text) for response in responses]
        print(f"Took {delta} s.")
    return delta


def get_time_for_requests(n_requests):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(_send_requests(n_requests))


def plot_time_per_n_requests(max_n_requests):
    all_n_requests = list(range(1, max_n_requests + 1))
    deltas = []
    for n_requests in all_n_requests:

        delta = get_time_for_requests(n_requests)
        deltas.append(delta)
        print(str(n_requests) + " on " + str(max_n_requests))
    plt.plot(all_n_requests, deltas)
    plt.xlabel("number of requests sent")
    plt.ylabel("time (s)")
    plt.show()


plot_time_per_n_requests(10)

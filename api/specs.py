"""HERE ARE ALL THE IMPORTANT VALUES."""
import os

USE_POSTGRES_ARTICLES = True
pwd = os.path.dirname(os.path.abspath(__file__))
USE_POSTGRES_SWIPESESSIONS = True

BACKEND_URL = "http://ec2-13-37-233-249.eu-west-3.compute.amazonaws.com:8080"


# At the end of the swipes, we look for all the articles cited by {candidate papers}
# U {positive seed papers}. We collect the RANGE_MOST_CITED_ARTICLES articles
# that are the most cited by {candidate papers} U {positive seed papers}, and we add
# them to the candidate papers.
RANGE_MOST_CITED_ARTICLES = 10


N_SIMILAR_ARTICLES = 5

N_FETCHED_ARTICLES_PER_QUESTION = 20

# for testing TODO augmenter toutes ces valeurs
MIN_COS_SIM_ARTICLE_QUESTION = 0.0001
# To find several articles answering question A in one of the end
# results, we call faiss on all the questions. We will then take
# the article associated with the simialar questions found by faiss.
# Faiss provides a score
# which indicates the quality of each result (here, a question B). This score must exceed
# the constant below in order for the item related to question B to be considered
# a good answer to question A.
MIN_SCORE_FOR_ARTICLES_ANSWERING_RELATED_QUESTIONS = 0.3

# Warning: this parameter is very sensitive.
# Even choosing 0.5 is very selective.
MIN_COS_SIM_QUESTION_QUERY = 0.4

THRESHOLD_FOR_QUESTIONS_CLUSTERING = 0.78

THRESHOLD_FOR_OTHER_ANSWERS = 0.78

# TODO set a higher threshold (0.6-0.7 ?) once
# the front will no longer bug when there is no hand question
MIN_SCORE_MAIN_ANSWER = 0.5

MAX_SIZE_WIKI_SUMMARY = 300

N_RELATED_TOPICS = 10

# # number of authors to display in the author tab
AUTHOR_TAB_SIZE = 25

MAX_N_ARTICLES_FOR_AUTHOR_EXPLORATION = 20


MAX_N_TOP_ARTICLES_CITED_TO_SHOW = 8

# we first fetch faiss on {N_ARTICLES_FAISS} articles, and ...
N_ARTICLES_FAISS = 120

# ... we keep the top {N_RETURNED_ARTICLES} with the best general_score
# (based on the faiss similarity with the query + year + nb in citations)
N_RETURNED_ARTICLES = 30


assert N_ARTICLES_FAISS >= N_RETURNED_ARTICLES


BONUS_SEMINAL = 0.1
MIN_N_ARTICLES_CITING_SEMINAL = 2

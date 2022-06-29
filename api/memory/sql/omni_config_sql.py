import os

import sqlalchemy
from sqlalchemy.orm.session import sessionmaker

from api.specs import USE_POSTGRES_ARTICLES

PG_USER = os.environ["PG_USER"]
PG_PASSWORD = os.environ["PG_PASSWORD"]
PG_PORT = os.environ["PG_PORT"]
PG_HOST = os.environ["PG_HOST"]

PG_DATABASE_ARTICLES = "postgres"

s2orc_version = "s2orc_metadata_20200705"
pipe_version = "ALL_FIELDS"

TABLE_NAME_ARTICLES = f"results_{pipe_version}_{s2orc_version}_origin"
TABLE_NAME_QUESTION_AND_TLDR = f"results_{pipe_version}_{s2orc_version}_res"


def get_engine_articles():
    """Return sqlalchemy engine"""
    if USE_POSTGRES_ARTICLES:
        engine_postgres = sqlalchemy.create_engine(
            f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE_ARTICLES}",  # noqa
            # pool_pre_ping=True,
        )
        return engine_postgres


session = sessionmaker(bind=get_engine_articles())()

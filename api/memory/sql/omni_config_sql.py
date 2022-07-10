import os
from typing import Callable, TypeVar
import psycopg2

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
    else:
        raise Exception()


session = sessionmaker(bind=get_engine_articles())()
session.close()

from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


# a decorator to start and close postre session
def start_db_session(func: F) -> F:
    def modified_func(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except:
            global session
            session = sessionmaker(bind=get_engine_articles())()
            res = func(*args, **kwargs)
            session.close()
            get_engine_articles().dispose()
        return res

    return modified_func  # type:ignore

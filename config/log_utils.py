import logging
from functools import wraps
from time import time

logging.basicConfig(filename="misc/log_access.txt", level=logging.DEBUG)


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        logging.info(f"Function {f.__name__} took {te-ts:2.4f} seconds")
        return result

    return wrap

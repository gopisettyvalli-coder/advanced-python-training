import logging
import time
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("%s started", func.__name__)
        try:
            return func(*args, **kwargs)
        finally:
            logging.info("%s completed", func.__name__)

    return wrapper


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logging.info(
                "%s took %.6f seconds",
                func.__name__,
                elapsed
            )

    return wrapper
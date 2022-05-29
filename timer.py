from functools import wraps
import time


def timer(func):

    @wraps(func)
    def wrapped(*args, **kwargs):
        ts = time.perf_counter()
        res = func(*args, **kwargs)
        te = time.perf_counter()
        print(f"{func.__name__} took {te-ts} s")
        return res

    return wrapped

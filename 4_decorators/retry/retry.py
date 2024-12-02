import time
from datetime import timedelta
from functools import wraps

def retry(count=3, delay=timedelta(seconds=1), handled_exceptions=(Exception,)):
    if count < 1:
        raise ValueError("count < 1")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as e:
                    last_exception = e
                    if attempt < count - 1:
                        time.sleep(delay.total_seconds())
            raise last_exception

        return wrapper

    return decorator

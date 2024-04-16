from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

logger.add(
                "my_log_file.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting function '{func.__name__}' with args {args} and kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' returned {result}")
            return result
        except Exception as e:
            logger.exception(f"Captured exception '{func.__name__}': {e}")
            raise  # Re-throws the exception to not change the behavior of the decorated function
    return wrapper
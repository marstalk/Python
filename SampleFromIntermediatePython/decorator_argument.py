#log decorator with argument to define logging file
from functools import wraps


def log_decorator(log_file="logFile.log"):
    def wrap_func(func):
        @wraps(func)
        def wrap_func2(*args, **kwargs):
            log_string = func.__name__ + "was called"
            print(log_string)
            with open(log_file, "a") as open_file:
                open_file.write(log_string + "\n")
        return wrap_func2
    return wrap_func


@log_decorator(log_file="log.log")
def find_user():
    pass


find_user()
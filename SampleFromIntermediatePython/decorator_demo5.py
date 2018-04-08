from functools import wraps

can_run = True

def my_decorator(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        if not can_run:
            return "function can not run" + kwargs["name"]
        else:
            return func()
    return new_func


@my_decorator
def say_hi():
    return "saying hi"


can_run = True
print(say_hi(name="mars"))

can_run = False
print(say_hi(name="mars"))


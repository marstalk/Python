from functools import wraps


def func_log(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(f.__name__ + " is called")
        return f(*args, **kwargs)
    return decorated


def decorator_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print("check auth")
        return f(*args, **kwargs)
    return decorated


@func_log
def add_function(a, b):
    return a + b


@decorator_auth
@func_log
def auth_login(name="mars"):
    return name + " login successfully"


print(add_function(3, 4))
print(auth_login("peter"))
print(auth_login())
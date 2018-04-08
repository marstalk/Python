

def a_new_decorator(func):

    def new_function():
        print("new function with decorator")
        func()
        print("end of new function with decorator")

    return new_function


def original_func():
    print("this is original function")


original_func()

original_func = a_new_decorator(original_func)

original_func()
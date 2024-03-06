from functools import wraps


def some_decorator(func):
    def _inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Something")
        return result
    return _inner_function

@some_decorator
def some_function_ver1():
    print("first")
    
def some_function_ver2():
    print("second")
    
some_function_ver1()
some_decorator(some_function_ver2)()

def proper_decorator(func):
    @wraps(func)
    def _inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Something proper")
        return result
    return _inner_function
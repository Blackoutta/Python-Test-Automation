import functools

# basic decorator
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("before func!")
        func(*args, **kwargs)
        print("after func!")
    return wrapper

@my_decorator
def my_function():
    print("I am the function!")

my_function()

## complex decorator
def decorator_with_args(number):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("before func!")
            if number == 56:
                print("not running the function")
            else:
                func(*args, **kwargs)
            print("after func!")
        return wrapper
    return my_decorator


@decorator_with_args(71)
def my_function_two(x,y):
    print(x+y)

my_function_two(20, 30)

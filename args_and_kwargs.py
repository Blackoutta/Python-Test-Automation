def my_long_method(*args):
    return sum(args)

# output = my_long_method(1,2,3,4,5,6,7,8,9)
# print(output)


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12,34,56, name="Jose", location="UK")

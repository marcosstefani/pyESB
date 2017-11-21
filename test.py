# def pass_thru(func_to_decorate):
#     def new_func(a, b, c):
#         print("Function has been decorated.  Congratulations.")
#         # Do whatever else you want here
#         return func_to_decorate(a, b, c)
#     return new_func


# @pass_thru
# def print_args(a, b, c):
#     print(a + b + c)


# print_args(1, 2, 3)

class ClassBasedDecoratorWithParams(object):

    def __init__(self, arg1, arg2):
        print("INIT ClassBasedDecoratorWithParams")
        print(arg1)
        print(arg2)

    def __call__(self, fn, *args, **kwargs):
        print("CALL ClassBasedDecoratorWithParams")

        def new_func(*args, **kwargs):
            print("Function has been decorated.  Congratulations.")
            return fn(*args, **kwargs)
        return new_func


@ClassBasedDecoratorWithParams("arg1", "arg2")
def print_args_again(*args):
    for arg in args:
        print(arg)


print_args_again(1, 2, 3)
print_args_again(1, 2, 3)
def custom_divide(func):
    def inner_func(a, b):
        if b > a:
            a, b = b, a
        return func(a, b)
    return inner_func

@custom_divide
def divide(a, b):
    print(a/b)

# divide = custom_divide(divide)
divide(2, 4)


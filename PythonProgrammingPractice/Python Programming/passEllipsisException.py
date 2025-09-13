# pass is usually used as a temporary keyword where a statement is required to avoid syntax errors.
# ... (or ellipsis) is usually used as a more permanent solution where a statement is required, but you don't want to implement it.
# raise NotImplementedError() is used as a reminder that the code hasn't been implemented
# and that it should be implemented soon (used more often in real situations)

def func1():
    pass


def func2():
    ...

# print(type(pass))
# print(type(...))

def func3():
    raise NotImplementedError("I'll come back to this at the end of the project")


func3()
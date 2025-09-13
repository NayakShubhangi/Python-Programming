def TryExceptFinallyKeywords(a, b):
    try:
        print(a + b)
    except:
        print("An exception occurred.")
    finally:
        print("The function has been run.")

# TryExceptFinallyKeywords("Str", "Str2")

import atexit

def printSomething():
    # You can use _ instead of a variable when you want a for loop, but don't need the variable
    for _ in range(3):
        print("Hello..")

# The atexit.register decorator makes it so that any function with this decorator runs after the main program is done,
# REGARDLESS of whether it runs successfully or has errors.
# It runs before the main program officially exits, similar to a finally block in try and except blocks.
# @atexit.register
# def exitHandler():
#     print("The printSomething() function has exited . . .")

# if __name__ == "__main__":
#     printSomething()
#     print(1/0)




# ONE:
# Why the output for this program is:
# Main program doing work...
# Third cleanup
# Second cleanup
# First cleanup

# and not:
# Main program doing work...
# First cleanup
# Second cleanup
# Third cleanup

# EXPLAINATION: The registered functions are called by how recently they were registered. (Kind of like Last in, First out in stacks)

@atexit.register
def first():
    print("First cleanup")

@atexit.register
def second():
    print("Second cleanup")

@atexit.register
def third():
    print("Third cleanup")

# atexit.register can also become a function. ALL decorators can be applied as functions.
# atexit.register(first)
# atexit.register(second)
# atexit.register(third)

print("Main program doing work...")
def func1():
    try:
        raise Exception
        return 0
    except:
        return 1
    finally:
        return 2

# print(func1())
# 2
# TASK FIVE (DONE):
# Explain why the output is 2:
# Finally can override return statements from both try and except.
# So, when the exception occurs and the line inside the except block runs,
# Python checks if there is a finally block, and since there is a finally block- which contains return 2,
# it overrides the return 1 statement in the except block.



e = 42
try:
    raise Exception('X')
except Exception as e:
    pass
# print(e)
# Error



a = 256
b = 256
# print(a is b)
c = 300
d = 300
# print(c is d)
# True
# True
# Explanation: Two of the same integer values will share memory



# TASK SIX (DONE):
# Come up with the expected output and and explain
print(3<4<5)
print(3<5<4)
# Expected Output:
# True
# False
# Explanation:
# 3 is less than 4 and 4 is less than 5, so the True and True results in True.
# 3 is less than 5, but 5 is not less than 4, so the True and False results in False.

# Come up with the expected output and and explain
a = {
     True: 'Yes',
     1: 'No',
     1.0: 'Maybe'}

print(a)
# Expected Output:
# {True: 'Maybe'}
# Explanation: All of these values- True, 1, and 1.0- are equal to True. So, each time, the value for True is overwritten, and
# since "Maybe" was the most recent overwrite, that will be the value corresponding to the key True.
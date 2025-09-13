# print(type([])==list)

# print("str"*-1)   # Any string multiplied by 0 or any number less than that will result in an empty string

# print(10++--++10)   # Multiple unary operators don't affect the value (you just find the right-side value), so this results in 10+10, which is 20
# print(5 + + + 3)
# print(--5)

# print({}==False)   # For 'containers' (lists, tuples, sets, dicts, str...), even if it's empty, the container is still there, so it would equal 1
# print(bool({}))   # Since the 'container' is empty, it will be False

# print(""==False)   # Strings are also containers, since they can be looped and store multiple characters
# print(bool(""))

# print(not not not False)   # not False = True => not True = False => not False = True
# print(not not not True)   # not True = False => not False = True => not True = False

# print("2"*3)   # Prints '2' 3 times
# print(3*"ABA")   # Order doesn't matter, so 'ABA' is printed 3 times

# print([] is [])   # False, because all containers (except for Tuple) are treated as different
# print([] == [])   # True

# a = frozenset({1, 2, 3})
# b = frozenset({1, 2, 3})
# print(a is b)   # False
# print(a == b)   # True

# print((1, 2, 3) is (1, 2, 3))   # True
# print((1,) == (1,))   # True

# print({1} is {1})   # False
# print({1} == {1})   # True

# print({} is {})   # False
# print({} == {})   # True

# a = 1
# b = 1
# print(a is b)   # True, because if the integer is the same, both variables will reference the same location

# a = 1.5
# b = 1.5
# print(a is b)   # True, because if the float is the same, both variables will reference the same location

# a = True
# b = True
# print(a is b)   # True, because if the boolean is the same, both variables will reference the same location

# a = "Str"
# b = "Str"
# print(a is b)   # True, because if the string is the same, both variables will reference the same location

# IN CONCLUSION, all mutable types return False for (# is #), while immutable types return True- EXCEPT FOR FROZENSET-
# Frozenset is a special case and returns False for some reason

# print(None is None)   # True, because None is immutable
# print(None==False)   # False
# print(None is False)   # False
# print(id(None))   # All Nonetypes have the same location
# print(id(False))   # All False types have the same location
# print(id(True))   # All True types have the same location
# print(id(2==2))   # Since this is True, this references the same location as True

# print(True+True+True)   # As a value, True is 1, so it results in 1+1+1, which is 3
# print(False+False+False)   # As a value, False is 0, so it results in 0+0+0, which is 0
# print(True+False+True+None)   # Nonetype isn't supported, and it will return an error

# print(type(True)==int)   # This is False, because even though we can perform operations with it, it is still a boolean type

# print(isinstance(True, int))   # True is an instance of integer, so it can be considered as an integer when performing operations

# print("a"<"b"<"c")   # Strings can be compared due to their ASCII value, and this would be True
# print(ord("A"))   # "a" = 97, "A" = 65
# print("A"<"b"<"C")   # False, since "b" > "C"

# print((1, 2)<(1, 3))   # First, it would compare whether 1 < 1, which is False,
# so it would continue to the next value and check whether 2 < 3, and since that is True, this statement is True
# print((1, 2, 3)<(1, 3))   # This statement is True because 2 < 3, and since that is True, it stops, and ignores the 3 on the left side
# print((1, 2, 3)<(1, 2, 3, 4))   # This statement is True because if the values are equal, it compares the number of elements
# print((0, 0, 0, 0)<(1, 2))   # This statement is True because 0 < 1, and despite the left side having more values, the right side is overall greater

# print([1, 2, 3]*0)   # This prints an empty list ([]), because if it's multiplied by 0 or any number less, it will be empty

# a = b = [1, 2, 3]
# a.append(4)
# print(b)   # Since both variables reference the same location due to having the same list, when one variable changes the list,
# the list is changed in the other variable as well


# TASK TWO: (DONE)
# Find out why the two lines of code below return [3, 3, 3, 3]
a = [lambda:i for i in range(4)]
print([f() for f in a])
# EXPLANATION: When f() is called, the for loop has finished and i holds its final value, which is 3.
# As a result, all lambda functions reference the same i variable which equals 3,
# meaning all functions return 3.


# d = {
#     True : "Yes",
#     1 : "No",
#     1.0: "Maybe"
# }
# print(d)   # Python saves the latest value, and since all of the keys equal True, python will only save the most recent value,
# which is {True: "Maybe"}

key = [1, 2]
d = {
    tuple(key): "Hello"
}
key.append(3)
# print(d)   # Once the tuple has its values, it will won't be affected by any changes since it's immutable. So: {(1, 2): "Hello"}
# print(key)

def foo(val):
    print("Foo was called")
    return val

# print(foo(False) or foo(True))
# Output:
# Foo was called
# Foo was called
# True
 
# functions = []
# for i in range(3):
#     def f():
#         return i
#     functions.append(f)
# print([func() for func in functions])   # Since multiple f()s are appended with different return values, each time the loop runs,
# the f()s will be overwritten with the most recent f(), and since f() with the return value of 2 is most recently appended,
# all three f()s will be changed to the f() that returns 2. As a result, the output is [2, 2, 2].
import copy

a = [[1, 2], [3, 4], 5]
# b = a[:]   # This is equal to having a = b = [[1, 2], [3, 4]] in the previous line
b = copy.deepcopy(a)
# b =                   # Figure out another way besides copy.deepcopy() to copy a variable to
# another variable without being able to change the first variable with the second variable (without looping)
b[0][0] = 100
# print(a)


# TASK ONE: (DONE)
# PART ONE:
# Get a brief understanding on self-hosted runner, types of runners, matrix, concurrency, and basic syntax of a github actions workflow
# Self-hosted runner: A system that you deploy and manage yourself to run GitHub Actions workflows.
# Types of runners: Two types- Github-hosted runners, and self-hosted runners.
# Matrix: Something that allows you to run the same job with different configurations.
# Concurrency: Something that allows you to control how many workflow runs or jobs can run simultaneously.
# Syntax (/ Mandatory things / Rules) of a Github Actions Workflow: Defined using YAML syntax,
# needs three core components:
# 1. name: A descriptive name for your workflow.
# 2. on: Specifies the events that trigger the workflow.
# 3. jobs: Defines the jobs that will run as part of the workflow.


# PART 2:
# Find how many ways a workflow can be run in on:
# There are 3 main ways:
#       1. MANUALLY, using the workflow_dispatch event,
# which lets you trigger a workflow directly from the GitHub UI or via the GitHub CLI.
#       2. ON A SCHEDULE, using the schedule event with cron syntax,
# which lets you define recurring times for your workflow to run.
#       3. ON SPECIFIC GITHUB EVENTS, by listening for various events that occur in your repository,
# organization, or even at an enterprise level.

# Find out whether a particular job can run parallel to another job. If yes, show how. Otherwise, explain why:
# By default, jobs in a GitHub Actions workflow run in parallel,
# unless you explicitly mention it.

# Find out what is 'needs' with its syntax (how it works and its syntax):
# needs is a keyword which definies the order of execution and dependencies between jobs in your workflow.
#
# Its value is either a single string (the ID of the job it depends on),
# or an array of strings (a list of job IDs it depends on).
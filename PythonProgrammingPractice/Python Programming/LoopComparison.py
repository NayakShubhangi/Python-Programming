# Write a program that will print sum of n-1 numbers where n is input
import timeit
import numpy

def while_loop(n:int=10_000_000):
    i=0
    result = 0
    while i < n:
        result += i
        i += 1
    return result

print("while_loop: ", while_loop(), timeit.timeit(while_loop, number=1))

def for_loop(n:int=10_000_000):
    result = 0
    for i in range(n):
        result += i
    return result

print("for_loop: ", for_loop(), timeit.timeit(for_loop, number=1))

def for_loop2(n:int=10_000_000):
    result = 0
    for i in range(n):
        if i < n:
            result += i
    return result

print("for_loop2: ", for_loop2(), timeit.timeit(for_loop2, number=1))

def range_loop(n:int=10_000_000):
    return sum(range(n))

print("range_loop: ", range_loop(), timeit.timeit(range_loop, number=1))

def numpy_range_loop(n:int=10_000_000):
    return sum(numpy.arange(n))

print("numpy_range_loop: ", numpy_range_loop(), timeit.timeit(numpy_range_loop, number=1))

def math_loop(n:int=10_000_000):
    return n*(n-1)//2

print("math_loop: ", math_loop(), timeit.timeit(math_loop, number=1))

# RESULT:
# while_loop:  49999995000000 0.8254230000002281
# for_loop:  49999995000000 0.5350575000002209
# for_loop2:  49999995000000 0.7026259999997819
# range_loop:  49999995000000 0.43887460000041756
# numpy_range_loop:  49999995000000 0.7655727999999726
# math_loop:  49999995000000 1.8000000636675395e-06

# 1. Math loop
# 2. Range loop
# 3. For loop
# 4. For loop (with conditionals)
# 5. Numpy loop
# 6. While loop

# timeit can be used to find the execution time of functions through timeit.timeit()
# which takes the function's name and how many times that function gets called
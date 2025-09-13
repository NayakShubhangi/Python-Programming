# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# n<1000
def fibonacci_nNum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Fn = Fn-1 + Fn-2
        return fibonacci_nNum(n-1) + fibonacci_nNum(n-2)

n = int(input("Enter a number: "))
print(fibonacci_nNum(n))

# If not one of the special cases, function finds the nth fibonacci number by recursively adding the (n-1)th and (n-2)th numbers together.
# EX:
# INPUT: n=5
# f(5) -> f(4) + f(3) -> 2+1=3       (3rd)
# f(4) -> f(3) + f(2) -> 1+1=2       (2nd)
# f(3) -> f(2) + f(1) -> 1+0=1       (1st)
# f(2) -> 1    (Special case: 2nd number is 1)
# f(1) -> 0    (Special case: 1st number is 0)
# OUTPUT: f(5) = 3

# In other words:
# f(5) -> 2 + 1 -> 3       (3rd)
# f(4) -> 1 + 1 -> 2       (2nd)
# f(3) -> 1 + 0 -> 1       (1st)
# f(2) -> 1    (Special case: 2nd number is 1)
# f(1) -> 0    (Special case: 1st number is 0)
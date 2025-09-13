# number = int(input("Enter a number: "))
# def IsPrime(number):
#     if number<=1:
#         return False
#     else:
#         for i in range(2, number):
#             if number%i == 0:
#                 return False
#                 break
#         else:
#             return True

# numbers = [int(i) for i in input("Enter two numbers separated by a space: ").split()]
# prime = []

# for i in range(numbers[0], numbers[1]):
#     if IsPrime(i) == True:
#         prime.append(i)
# print(prime)

# Factorial of five = 5*4*3*2*1

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
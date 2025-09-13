n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

j = 1
def IsPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True


while j < n+1:
    if IsPrime(j) == True:
        pass
    else:
        print(j)
    j += 1
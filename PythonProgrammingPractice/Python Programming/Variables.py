Variable = 5
variable = "String"
_Variable = 10.7
ComplexVar = 4+3j
BoolVar = True
BoolVar2 = False

print(Variable, variable, _Variable, sep="&")
if(-1):
    print(BoolVar2)
while(Variable!=0):
    Variable-=1
    print("True")
for i in range(11):
    print(i)
print(list(range(1, 11, 3)))
print(list(range(1, 100, 2)))

Name = "Shubhangi"
Var = 8
print("Hi {1} {0}".format(Name, Var))
print(bool(Variable))
a = 0
b = 1
a, b = b, a
print(a, b)
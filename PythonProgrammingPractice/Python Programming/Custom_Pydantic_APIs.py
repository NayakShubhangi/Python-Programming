class Custom_One(Exception):
    "Exception Occured: Among a, b, c, one of them is 'vulnerable'"
    pass



a = input("Enter a value: ")
b = input("Enter another value: ")
c = input("Enter a last value: ")
def Func1(a, b, c):
    try:
        if (a.lower() == "vulnerable") or (b.lower() == "vulnerable") or (c.lower() == "vulnerable"):
            raise Custom_One
        else:
            print("No exception raised...")
    except Custom_One as ex:
        print(f"{ex}")
Func1(a, b, c)
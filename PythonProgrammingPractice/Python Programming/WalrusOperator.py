# The walrus operator is used to validate the condition and assign a value at the same time.

dict1: dict[str, int | None] = {
    "key1": 1,
    "key2": 2,
    "key3": None
}

# WITHOUT WALRUS OPERATOR:
# keyNum = input("Enter either key1, key2, or key3: ")
# keyVar = 0
# if dict1[keyNum] != None:
#     keyVar = dict1.get(keyNum)
#     print(keyVar)
# else:
#     print("The key's value is None")


# WITH WALRUS OPERATOR:
# if dict1.get(keyVar:=input("Enter either key1, key2, or key3: ")) != None:
#     # First, keyVar equals the input, then the .get(keyVar) is checked against None
#     print(dict1.get(keyVar))
# else:
#     print("The key's value is None.")


# TASK ONE:
# Come up with two examples for the walrus operator

# while (user_input := input("Enter something (Type 'exit' to quit): ")).lower() != 'exit':
#     print(f"You entered: {user_input}")
# print("You typed exit. End of program.")


while (length := len(user_input := input("Enter a string that is at least 5 characters long: "))) < 5:
    print(f"The input is too short! Length: {length}")
print(f"Valid input: {user_input}")
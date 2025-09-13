dict1 = {
    "key" : "value",
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4",
    (1, 2, 3) : "value5",
    "key6" : {"key1" : "value1", "key2" : "value2"}
}
# print(dict1["key6"]["key2"])
print(dict1.setdefault("key7", "value10"))
print(dict1)
# print(dict1)
# print(dict1["key1"])
# print(dict1.get("key7"))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# print(dict1)
# dict1[(1, 2, 3)] = "value6"
# print(dict1)
# dict1["key5"] = "value5"
# print(dict1)
# print(dict1.get("key6"))
# dict1.update({"key" : "value9"})
# print(dict1)
# for i in dict1:
#     print(i, dict1[i])

# user_key = input("Enter a key: ")
# if dict1.get(user_key) != None:
#     print(dict1.get(user_key))
# else:
#     print("There is no value assigned to that key.")
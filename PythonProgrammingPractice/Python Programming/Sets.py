set1 = {1, "Two", False, 1, False, False, True, True, 0}
set2 = set()
print(set1)
print(int(True))
print(type(set2))
def FindDuplicate(parameter):
    set3 = set()
    for i in parameter:
        if (parameter.count(i)>1):
            set3.add(i)
    return set3
print(FindDuplicate((1, 1, "Three", 4, True, False, False)))
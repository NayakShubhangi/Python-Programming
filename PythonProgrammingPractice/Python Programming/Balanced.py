def is_balanced(string):
    open_parentheses = 0
    open_square = 0
    open_curly = 0

    for i in string:
        if i == "(":
            open_parentheses += 1
        elif i == "[":
             open_square += 1
        elif i == "{":
             open_curly += 1
        elif i == ")":
            open_parentheses -= 1
            if open_parentheses < 0:
                    return False
        elif i == "]":
             open_square -= 1
             if open_square < 0:
                  return False
        else:
             open_curly -= 1
             if open_curly < 0:
                  return False
    if open_parentheses < 0 or open_parentheses > 0:
        return False
    return True

string1 = "{}[]({)}"
if is_balanced(string1):
    print(f'The string "{string1}" is balanced.')
else:
    print(f'The string "{string1}" is imbalanced.')

# ]()[ -> Imbalanced (needs to be opened first before closing, not the other way around)
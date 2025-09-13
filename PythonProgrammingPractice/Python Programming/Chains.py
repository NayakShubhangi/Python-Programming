# A<B>C<D
# Ex: [1, 4, 3, 2] -> [1, 4, 2, 3]
#                      A  B  C  D
# Can be more than 4 digits: ...D>E<F>G<H>I...
# def rearrange_list(arr):
#     for i in range(1, len(arr) - 1, 2):
#         if arr[i - 1] >= arr[i]:
#             arr[i - 1], arr[i] = arr[i], arr[i - 1]
#         if arr[i + 1] >= arr[i]:
#             arr[i + 1], arr[i] = arr[i], arr[i + 1]
#     return arr
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print("\nOriginal list:", list1)
# result = rearrange_list(list1)
# print("Rearranged list:", result)


# Ex: "My name is apple" -> A=1 -> Z=26
# Replace every character with the numerical number
# M=13 -> (13)..y name is apple
def replace_with_alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            position = ord(char.lower()) - ord('a') + 1
            result.append(f"({position})")
        else:
            result.append(char)
    return ''.join(result)
string1 = "--Hello"
print("Original string:", string1)
result = replace_with_alphabet_position(string1)
print("Converted string:", result)
import sys


def check_for_consecutive_letters(word, letters):
    return letters in word


def sort_based_on_letter_position(words, letter):
    return sorted(words, key=lambda word: word.find(letter) if word.find(letter) != -1 else len(word))


def split_and_sort(words, letters, index):
    contains_letters = []
    does_not_contain_letters = []
    for word in words:
        word = word.strip()
        if check_for_consecutive_letters(word, letters):
            contains_letters.append(word)
        else:
            does_not_contain_letters.append(word)
    if contains_letters and index < len(contains_letters[0]):
        letter_to_sort_by = contains_letters[0][index].lower()  # Use lower() for case-insensitive comparison
        sorted_contains_letters = sort_based_on_letter_position(contains_letters, letter_to_sort_by)
    else:
        sorted_contains_letters = contains_letters

    return sorted_contains_letters, does_not_contain_letters


if __name__ == "__main__":
    words = sys.argv[1].split(',')
    letters = sys.argv[2]
    try:
        index = int(sys.argv[3])
    except ValueError:
        print(f"Error: The provided index '{sys.argv[3]}' is not a valid number.")
        sys.exit(1)
    contains, does_not_contain = split_and_sort(words, letters, index)
    print(f"Words that contain '{letters}': {contains}")
    print(f"Words that don't contain '{letters}': {does_not_contain}")
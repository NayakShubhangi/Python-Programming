# TASK TWO
# Read the .txt file provided and give the number of occurrences of each word and the number of spaces
# Add python script in jenkins, and give parameter so that you can upload a file to jenkins, and jenkins will run a python script to do the rest.
# EX: a .txt file given by the user says "The user name is user" -> *Dictionary will be returned and key would be each word, while value would be number of occurences*
# -> *4 different words, so 4 keys and 4 values* -> The: 1, User: 2, name: 1, is: 1 -> *Number of spaces should be provided as well* -> Spaces: 4
import sys
from collections import Counter

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    word_count = Counter(words)
    space_count = text.count(' ')
    word_count['Spaces'] = space_count
    return dict(word_count)

if __name__ == "__main__":
    file_path = sys.argv[2]
    print(file_path)
    print(sys.argv[1])
    result = process_text_file(file_path)
    print(result)
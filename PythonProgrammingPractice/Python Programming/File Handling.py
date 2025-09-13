# Three modes: Read, Append, Write
# Read Parameters: File should exist (or error occurs)
# Append Parameters: If file doesn't exist, append creates one
# Write Parameters: If file doesn't exist, write creates one
# var = open("variables.txt", "a")
# var.write("\nHappy Birthday")
# var.close()
# var = open("variables.txt", "r")
# print(var.read(17))
# var.close()

import os

def fileuse():
    filename = input("Enter the name of the file: ")
    filecontent = input("Enter the content for the file: ")
    if os.path.exists(filename):
        userfile = open(filename, "a")
    else:
        userfile = open(filename, "w")
    userfile.write(f"\n{filecontent}")
    userfile.close()
    userfile = open(filename, "r")
    print(userfile.read())
    userfile.close()

fileuse()
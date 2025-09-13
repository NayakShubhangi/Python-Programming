import getpass
import os


def readfunc(filename):
    openfile = open(filename, "r")
    contentFile = openfile.read()
    openfile.close()
    return contentFile


def readlinesfunc(filename):
    openfile = open(filename, "r")
    contentFile = openfile.readlines()
    openfile.close()
    return contentFile


def appendfunc(filename, content):
    openfile = open(filename, "a")
    openfile.write(content + "\n")
    openfile.close()
    contentFile = readfunc(filename)
    return contentFile


def writefunc(filename, content):
    openfile = open(filename, "w")
    openfile.write(content)
    openfile.close()
    contentFile = readfunc(filename)
    return contentFile


def createfile(username):
    filename = input("What is the name of the file (include .txt): ")
    while checkfileexists(filename):
        filename = input(f"The file '{filename}' already exists. Please enter a different filename: ")
    writefunc(filename, "")
    appendfunc("file_owners.txt", f"{filename}: {username}")
    print(f"File '{filename}' created.")


def modifyfile(username):
    filename = input("What is the name of the file (include .txt): ")
    if checkfileowner(filename, username):
        content = input("Enter the content you want appended to the file: ")
        print(appendfunc(filename, content))
        print(f"File '{filename}' modified.")
    else:
        print("You do not have permission to modify this file.")


def deletefile(username):
    filename = input("What is the name of the file (include .txt): ")
    if checkfileowner(filename, username):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted.")
            updatefileowners(filename)
        else:
            print(f"The file '{filename}' doesn't exist.")
    else:
        print("You do not have permission to delete this file.")


def checkfileowner(filename, username):
    if os.path.exists("file_owners.txt"):
        file_owners = readlinesfunc("file_owners.txt")
        for line in file_owners:
            file, owner = line.strip().split(": ")
            if file == filename and owner == username:
                return True
    return False


def updatefileowners(filename):
    if os.path.exists("file_owners.txt"):
        file_owners = readlinesfunc("file_owners.txt")
        openfile = open("file_owners.txt", "w")
        for line in file_owners:
            if not line.startswith(filename):
                openfile.write(line)
        openfile.close()


def checkfileexists(filename):
    return os.path.exists(filename)


def validation(username, password):
    fileContent = readlinesfunc("login.txt")
    usernames = [line.strip().split(": ")[1] for line in fileContent[1::4]]
    passwords = [line.strip().split(": ")[1] for line in fileContent[2::4]]
    for i, j in zip(usernames, passwords):
        if i == username and j == password:
            return True
    return False


def signup():
    name = input("What is your name: ")
    username = input("What is your username: ")
    password = getpass.getpass("What is your password: ")
    if validation(username, password):
        print("This username is already taken.")
        login()
        return False
    content = f"name: {name}\nusername: {username}\npassword: {password}\n\n"
    appendfunc("login.txt", content)
    print("Account created successfully.")
    return True


def login():
    username = input("What is your username: ")
    password = getpass.getpass("What is your password: ")
    if validation(username, password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return False


def main():
    print("Welcome to the program")
    con = input("Do you have an existing account (Yes or No): ")
    if con.lower() == "yes":
        chances = 2
        while chances > 0:
            username = login()
            if username:
                break
            else:
                chances -= 1
                if chances > 0:
                    print("Retrying... Please enter valid credentials.")
                else:
                    print("No more attempts left.")
        if not username:
            print("Redirecting to signup...")
            signup()
            username = login()
        if username:
            op = input("""Would you like to create, modify, or delete a file?
                       To create, press 1
                       To modify, press 2
                       To delete, press 3
                       > """)
            match op:
                case "1":
                    createfile(username)
                case "2":
                    modifyfile(username)
                case "3":
                    deletefile(username)
                case _:
                    print("You have entered an invalid operation.")
    elif con.lower() == "no":
        if signup():
            username = login()
            if username:
                op = input("""Would you like to create, modify, or delete a file?
                           To create, press 1
                           To modify, press 2
                           To delete, press 3
                           > """)
                match op:
                    case "1":
                        createfile(username)
                    case "2":
                        modifyfile(username)
                    case "3":
                        deletefile(username)
                    case _:
                        print("You have entered an invalid operation.")
    else:
        print("You have entered an invalid answer.")


main()
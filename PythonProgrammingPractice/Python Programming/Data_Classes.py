# # class Class1:
# #     def __init__(self, a : str, b : str, c : str):
# #         self.a = a
# #         self.b = b
# #         self.c = c

# # obj : Class1 = Class1("A", "B", "C")
# # print(Class1)

# from dataclasses import dataclass, field

# # Dataclasses are useful in python to reduce lines of code, provide customization for classes, and provide high-level GUI/UI
# @ dataclass
# class Person:
#     a : str
#     b : str
#     c : str = field(init = False, repr = False)
    
#     def __post_init__(self):
#         self.c = "D"

# # Field is a built-in function in dataclass that provides flexibility to hide instance variables by using "init = False"
# # For another layer of hiddenness- to avoid it being displayed when you print the object, use "repr = False"
# # If you want to hide an instance variable, you define their value through __post_init__
# obj = Person("A", "B")
# print(obj.a, obj.b)
# print(obj.c)
# print(obj)



# For ANOTHER layer of protection, we can add (frozen = True) to the annotation of dataclass, which will "freeze" the instance variables,
# which will make them be unable to be changed, UNLESS you change them when you initially create an object.
# YET ANOTHER layer of protection can be added through "kw_only = True" which will only allow you to change them in
# the initial creation of an object by using keyword arguments.
# @ dataclass(frozen = True, kw_only = True)
# class Student:
#     roll_num : int = 123
#     # marks : float = field(repr = False)
#     subject : str = "Mathematics"


# student1 = Student(roll_num = 132, subject = "Math")
# print(student1)
# user = eval(input("> "))
# if user.lower() == "authorized":
#     print(student1.marks)

# student1.roll_num = 456
# print(student1)





# TASK ONE:
# Create a table named "bank_account" in MYSQL, which will have columns "Current_Balance", "Name", "Age", "Bank_Name", "Password", which
# will have 5 records in them.
# Then, create a class named "bank_account" in Python, which should have everything that is in the "bank_account" table, except "Password"
# should be hidden by using (repr = False) & (init = False).
# After that, make a function named "login", which should ask for the name and password from the user.
# If the given name and password matches the information in the table, user is allowed to display their bank account details (by printing
# the object). take note: password is hidden from the user, so it should not show when the object is printed

# TASK ONE
# Out of the five records inputed, want to update one of them in the MySQL database
# Use post API from FastAPI to change any of the five values (balance, name, age, bank, or password) and and the updated value is
# updated in the database itself

import mysql.connector

mysql_connector = mysql.connector.connect(host="localhost", user="Amrit", password="PariShubhangi24")
mysql_cursor = mysql_connector.cursor()
# mysql_cursor.execute("CREATE DATABASE Bank")
mysql_cursor.execute("use Bank")
# mysql_cursor.execute("CREATE TABLE bank_account (Current_Balance DECIMAL(10, 2), Name VARCHAR(50), Age INT, Bank_Name VARCHAR(50), Password VARCHAR(50))")
# bank_var = "INSERT INTO bank_account (Current_Balance, Name, Age, Bank_Name, Password) values (%s, %s, %s, %s, %s)"
# bank_values = [
#     (1000.50, 'John Doe', 30, 'Chase', 'password123'),
#     (2500.75, 'Jane Smith', 28, 'Bank of America', 'jsmith456'),
#     (1800.00, 'Mark Taylor', 35, 'Wells Fargo', 'mtaylor789'),
#     (3200.90, 'Alice Johnson', 32, 'Citibank', 'alicej890'),
#     (1500.10, 'David Lee', 40, 'Chase', 'dlee567')
# ]
# mysql_cursor.executemany(bank_var, bank_values)
# mysql_connector.commit()
# mysql_connector.close()
from fastapi import FastAPI, HTTPException, Request
from getpass import getpass
import mysql.connector

app = FastAPI()

class BankAccount:
    def __init__(self, current_balance, name, age, bank_name):
        self.current_balance = current_balance
        self.name = name
        self.age = age
        self.bank_name = bank_name
        self._password = None

    def set_password(self, password):
        self._password = password

    def login(self):
        input_name = input("Enter your name: ")
        input_password = getpass("Enter your password: ")

        if input_name == self.name and input_password == self._password:
            print(f"Login successful! Welcome, {self.name}.")
            print(self)
        else:
            print("Login failed. Incorrect name or password.")

    def __repr__(self):
        return f"BankAccount(Name: {self.name}, Age: {self.age}, Bank: {self.bank_name}, Current Balance: ${self.current_balance:.2f})"


def fetch_user_from_db(name):
    query = "SELECT Current_Balance, Name, Age, Bank_Name, Password FROM bank_account WHERE Name = %s"
    mysql_cursor.execute(query, (name,))
    result = mysql_cursor.fetchone()

    if result:
        current_balance, name, age, bank_name, password = result
        user_account = BankAccount(current_balance, name, age, bank_name)
        user_account.set_password(password)
        return user_account
    else:
        print("User not found.")
        mysql_connector.close()
        return None


@app.post("/update_account/")
async def update_account(request: Request):
    data = await request.json()
    # await makes the computer 'wait' until a request happens (in this case, in the form of json).
    # To use await, the async keyword is required.
    # There are two types of functions, synchronus and asynchronus.
    # By default, a function is synchronus, so to make it asyhconrus, you have to use the async keyword.
    name = data.get("name")
    field = data.get("field")
    new_value = data.get("new_value")
    user = fetch_user_from_db(name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    valid_fields = {"Current_Balance", "Name", "Age", "Bank_Name", "Password"}
    if field not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid field")

    query = f"UPDATE bank_account SET {field} = %s WHERE Name = %s"
    
    try:
        mysql_cursor.execute(query, (new_value, name))
        mysql_connector.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error updating account: " + str(e))

    return {"message": f"{field} successfully updated for {name}"}


def main():
    name = input("Enter your name to fetch your account: ")
    user_account = fetch_user_from_db(name)
    
    if user_account:
        user_account.login()


if __name__ == "__main__":
    main()
# Signup, login
# Signup- User needs three things, User's name, username (database name), password
# Create, update, delete
import getpass
import mysql.connector

class Notepad():
    def signup(self):
        self.name = input("Enter your name: ")
        self.username = input("Enter your preferred username: ")
        self.password = getpass.getpass()
        self.db_setup()
        self.write_query(f"create database {self.username}")
        print("Successfully created database. . .")
        # Credentials_db, notepad users- name, username, password
        self.execute_query("use Credentials_db")
        self.execute_query(f"insert into notepad_users(Name, Username, Password) values ({self.name}, {self.username}, {self.password})")
        print(f"Sucessfully inserted {self.name}'s data. . .")
        self.db_close()
    
    def login(self):
        self.name = input("Enter your name: ")
        self.username = input("Enter your preferred username: ")
        self.password = getpass.getpass()
        self.db_setup()
        self.execute_query("use Credentials_db")
        self.read_query(f"select * from Notepad_Users where Name = {self.name} and Username = {self.username} and Password = {self.password}")
        print("Successfully logged in. . .")
        self.db_close()

    def db_setup(self):
        self.sql_connection = mysql.connector.connect(host="localhost", user="Amrit", password="PariShubhangi24")
        self.sql_cursor = self.sql_connection.cursor()
    
    def db_close(self):
        self.sql_connection.close()
    
    def write_query(self, query):
        self.sql_cursor.execute(query)
        self.sql_connection.commit()
    
    def read_query(self, query):
        data = self.sql_cursor.execute(query)
        print(data)

    def execute_query(self, query):
        self.sql_cursor.execute(query)

notepad_obj = Notepad()
notepad_obj.signup()
notepad_obj.login()
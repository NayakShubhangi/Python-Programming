# The hiarchy starts from the database -> tables -> table -> columns -> rows -> records

import mysql.connector

mysql_connector = mysql.connector.connect(host="localhost", user="Amrit", password="PariShubhangi24")
mysql_cursor = mysql_connector.cursor()
# Query to create a database is "create database <database_name>"
# Query to pick up a database is "use <database_name>"

# mysql_cursor.execute("use python_practice")
# Query to create a table is "create table <table_name> (<name_of_column> <type_of_column>(<size_of_column>))"
# mysql_cursor.execute("create table learners (name VARCHAR(255), courses VARCHAR(255))")
# var = "insert into learners (name, courses) values (%s, %s)"
# values = ("Bob", "Python")
# mysql_cursor.execute(var, values)

# If you want to insert something into database and preserve the data, use "<connection_variable>.commit()"
# mysql_connector.commit()

# print(mysql_cursor.rowcount, "Insert successful")
# mysql_cursor.execute("select * from learners")
# var = mysql_cursor.fetchall()
# print(var)
# mysql_connector.close()
# Query to insert into table is "insert into <table_name> (<name_of_column>) values (<value_of_column>)"
# The purpose of mysql_connector.close() is to end the server connection when we are done




# TASK:
# Create a new database and insert three tables
# In each table, insert at least five records and display them

# mysql_cursor.execute("create database School")
mysql_cursor.execute("use School")

# mysql_cursor.execute("CREATE TABLE Students (StudentID INT, FirstName VARCHAR(50), LastName VARCHAR(50), GradeLevel INT)")
# mysql_cursor.execute("create table Courses (CourseID INT, CourseName VARCHAR(100), Teacher VARCHAR(50))")
# mysql_cursor.execute("create table Enrollments (EnrollmentID INT, StudentID INT, CourseID INT, EnrollmentDate DATE)")

students_var = "insert into Students (StudentID, FirstName, LastName, GradeLevel) values (%s, %s, %s, %s)"
students_values = [
    (1, 'John', 'Doe', 7),
    (2, 'Emma', 'Watson', 8),
    (3, 'Liam', 'Smith', 7),
    (4, 'Olivia', 'Brown', 8),
    (5, 'Noah', 'Johnson', 7)
]
mysql_cursor.executemany(students_var, students_values)
mysql_connector.commit()

courses_var = "insert into Courses (CourseID, CourseName, Teacher) values (%s, %s, %s)"
courses_values = [
    (101, 'Mathematics', 'Mr. Allen'),
    (102, 'Science', 'Ms. Clark'),
    (103, 'History', 'Mr. Adams'),
    (104, 'English', 'Mrs. Baker'),
    (105, 'Art', 'Ms. Davis')
]
mysql_cursor.executemany(courses_var, courses_values)
mysql_connector.commit()

enrollments_var = "insert into Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate) values (%s, %s, %s, %s)"
enrollments_values = [
    (1, 1, 101, '2024-09-01'),
    (2, 2, 102, '2024-09-01'),
    (3, 3, 103, '2024-09-02'),
    (4, 4, 104, '2024-09-03'),
    (5, 5, 105, '2024-09-04')
]
mysql_cursor.executemany(enrollments_var, enrollments_values)
mysql_connector.commit()
print(f"{mysql_cursor.rowcount} Insert successful")

mysql_cursor.execute("select * from Students")
students = mysql_cursor.fetchall()
print("Students:", students)

mysql_cursor.execute("select * from Courses")
courses = mysql_cursor.fetchall()
print("Courses:", courses)

mysql_cursor.execute("select * from Enrollments")
enrollments = mysql_cursor.fetchall()
print("Enrollments:", enrollments)

mysql_connector.close()
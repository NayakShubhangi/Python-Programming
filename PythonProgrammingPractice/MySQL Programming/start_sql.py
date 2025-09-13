# MySQL is a structured-query language that operates in a server
# An SQL allows the user to store their data in the form of tables

# How to connect with MySQL using Python
# Needs a connector to connect
# Needs a cursor to execute the queries and operate the results
# Use pip install to download connector when it is first time (pip install mysql-connector-python)

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Amrit", password="PariShubhangi24")
mysql_cursor = mydb.cursor()
mysql_cursor.execute("show databases")
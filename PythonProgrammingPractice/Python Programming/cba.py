import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Amrit", password="PariShubhangi24")
mysql_cursor = mydb.cursor()
mysql_cursor.execute("SHOW DATABASES")
var = mysql_cursor.fetchall()
print(var)
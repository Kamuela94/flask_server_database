import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="somewhereovertherainbow",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE schorrdatabase")
mycursor.execute("CREATE TABLE schorrtable (schorrId INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), address VARCHAR(255), state VARCHAR(255), company VARCHAR(255),)")

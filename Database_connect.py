import os
import mysql.connector

mydb = mysql.connector.connect(
host= '18.136.157.135',
user= 'dm_team10',
password= 'DM!$!Team!92@05!156&',
port= '3306',
database= 'project_movie_database'
)

sql= "select * from directors"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()
print (myresult) 



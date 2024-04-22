import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'buildAI1!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dbname")

print("All done!")
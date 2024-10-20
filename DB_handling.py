import mysql.connector

db = mysql.connector.connect(
    host="sql8.freesqldatabase.com",
    user="sql8738001",
    password="47ZRedGlmv",
    database="sql8738001"
)

cursor = db.cursor()

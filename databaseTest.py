import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Shiven@12",
    database="facial_recognition_attendance",
)
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("connection Succesfully created!")

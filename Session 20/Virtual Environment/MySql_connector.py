import mysql.connector as db


print("Connecting to MySQL database...")
connection = db.connect(
    username='root',
    password='himanshu',
    host='127.0.0.1',
    database = 'testing'
)
print("Connected to MySQL database.")
cursor = connection.cursor()

# query = "INSERT INTO test VALUES(null, 'John','john@gmail.com')"
sql = 'SELECT * FROM test'

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row)
connection.commit()
print("Data inserted successfully.")

cursor.close()
connection.close()
print("Connection closed.")
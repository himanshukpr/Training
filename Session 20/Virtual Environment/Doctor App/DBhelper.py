# controller


import mysql.connector as db

class DBhelper:
    def __init__(self):
        self.connection = connection = db.connect(
                            username='root',
                            password='himanshu',
                            host='127.0.0.1',
                            database = 'training'
                            )


        self.cursor = self.connection.cursor()
        print("Database connection established successfully.")

    def write(self,sql_query):
        print("Executing SQL query:", sql_query)
        self.cursor.execute(sql_query)
        print("(write) sql query executed successfully.")
        self.connection.commit()


    def read(self,sql_query):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        print("(read) sql query executed successfully.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return rows
    
    def close(self):
        print("Closing connection to database...")
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")
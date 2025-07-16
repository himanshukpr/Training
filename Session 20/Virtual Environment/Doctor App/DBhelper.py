# controller


import mysql.connector as db

class DBhelper:
    def __init__(self, username, password, host, database):
        self.connection = connection = db.connect(
                            username=username,
                            password=password,
                            host=host,
                            database = database
                            )


        self.cursor = self.connection.cursor()
        print("Database connection established successfully.")

    def write(self,sql_query):
        print("Executing SQL query:", sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()
        print("(write) sql query executed successfully.")


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
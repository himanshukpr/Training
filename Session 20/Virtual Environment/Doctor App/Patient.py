"""

doctor's app
------------------------
patient
consulation


patient - p_id, name, phone, email, dob, gender, created_on

sql = CREATE TABLE  patients (p_id INTEGER PRIMARY KEY auto_increment, 
                                name TEXT, 
                                phone TEXT, 
                                email TEXT, 
                                dob DATE, 
                                gender TEXT,
                                created_on datetime
                                );

        INSERT INTO patients VALUES(NULL, 'Himanshu', '1234567890', 'himanshu@gmail.com', '1990-01-01', 'Male', datetime.datetime.now())

"""

# model or object or entity
import datetime

class Patient:
    def __init__(self, name=None, phone=None, email=None, dob=None, gender=None):
        self.p_id = 0
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.gender = gender
        self.created_on = None

    def input_patient(self):
        self.name = input("Enter Name: ")
        self.phone = input("Enter Phone: ")
        self.email = input("Enter Email: ")
        self.dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        self.gender = input("Enter the Gender: ")
        self.created_on = datetime.datetime.now()

    def display_patient(self):
        print("~~~~~~~~~~~~~Patient Details:~~~~~~~~~~~~~")
        print(f"Patient ID: {self.p_id}")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"DOB: {self.dob}")
        print(f"Gender: {self.gender}")
        print(f"Created On: {self.created_on}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
"""

doctor's app
------------------------
patient
consulation

consulation = c_id,

sql = CREATE TABLE consulation ( c_id int PRIMARY KEY auto_increment,
                                p_id int,
                                remarks TEXT,
                                medicine TEXT,
                                followup datetime,
                                created_on datetime
                                foreign key (p_id) references patients(p_id)
                            );



"""
import datetime

class Consultation:
    def __init__(self, remarks=None, medicine=None, followup=None):
        self.c_id = 0
        self.p_id = 0
        self.remarks = remarks
        self.medicine = medicine
        self.followup = followup
        self.created_on = datetime.datetime.now()

    def input_consultation(self):
        self.remarks = input("Enter Remarks: ")
        self.medicine = input("Enter Medicine: ")
        self.followup = input("Enter Follow-up Date (YYYY-MM-DD HH:MM:SS): ")


    def show(self):
        print("~~~~~~~~~~~~~Consultation Details:~~~~~~~~~~~~~")
        print(f"Consultation ID: {self.c_id}")
        print(f"Patient ID: {self.p_id}")
        print(f"Remarks: {self.remarks}")
        print(f"Medicine: {self.medicine}")
        print(f"Follow-up: {self.followup}")
        print(f"Created On: {self.created_on}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

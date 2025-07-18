# view + controller
import datetime
from DBhelper import DBhelper
from Patient import Patient
from Consultation import Consultation


class DoctorsApp:
    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('Welcome to doctors app')
        print('App stated at',datetime.datetime.now())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        self.db_helper = DBhelper(
                                    username='root',
                                    password='himanshu',
                                    host='127.0.0.1',
                                    database = 'training'
                                )   


    def show_main_menu(self):
        while True:
            print("1. For Patient")
            print("2. For Consultation")
            print("0. Quit")
            choice = int(input('Enter you choice: '))
            if choice == 1:
                self.show_patient_menu()
            elif choice == 2:
                self.show_consultation_menu()
            elif choice == 0:
                self.db_helper.close()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Thanks for using doctors app')
                print('App ended at',datetime.datetime.now())
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
            else:
                print("Invalid choice")
                
    def show_patient_menu(self):
        while True:
            print("1. Add new Patient")
            print("2. Update Existing Patient")
            print("3. Delete Existing Patient")
            print("4. Fetch All Existing Patient")
            print("5. Fetch Patient by Phone Number")
            print("6. Fetch Male Patient")
            print("7. Fetch Female Patient")
            print("8. Fetch Patient by created date (Sort)")
            print("0. Quit")
            choice = int(input('Enter you choice: '))
            if choice == 1:
                patient = Patient()
                patient.input_patient()

                sql_query = f"INSERT INTO patients VALUES(NULL, '{patient.name}', '{patient.phone}', '{patient.email}', '{patient.dob}', '{patient.gender}', '{patient.created_on}')"
                self.db_helper.write(sql_query)

            elif choice == 2:
                
                p_id = int(input("Enter the id: "))
                sql_query = f"select * from patients where p_id={p_id}"
                rows = self.db_helper.read(sql_query)
                if len(rows) != 0:
                    patient = Patient()
                    patient.p_id = rows[0][0]
                    patient.name = rows[0][1]
                    patient.phone = rows[0][2]
                    patient.email = rows[0][3]
                    patient.dob = rows[0][4]
                    patient.gender = rows[0][5]

                    patient.display_patient()

                    name = input("Enter new name: ")
                    if len(name)!=0:
                        patient.name = name

                    phone = input("Enter new phone no: ")
                    if len(phone)!=0:
                        patient.phone = phone

                    email = input("Enter new email: ")
                    if len(email)!=0:
                        patient.email = email
                        
                    dob = input("Enter new dob: ")
                    if len(dob)!=0:
                        patient.dob = dob

                    gender = input("Enter new gender: ")
                    if len(gender)!=0:
                        patient.gender = gender

                    sql_query = "update patients set name='{}',phone='{}', email='{}',dob='{}',gender='{}' where p_id={}".format(
                        patient.name,
                        patient.phone,
                        patient.email,
                        patient.dob,
                        patient.gender,
                        patient.p_id
                    )

                    self.db_helper.write(sql_query)

            elif choice == 3:
                p_id = int(input("Enter Patient ID to delete: "))
                sql_query = f"DELETE FROM patients WHERE p_id = {p_id}"
                self.db_helper.write(sql_query)

            elif choice == 4:
                sql_query = "SELECT * FROM patients"
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for row in rows:
                    print(row)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            elif choice == 5:
                phone_no = input("Enter Phone Number to search: ")
                sql_query = f"SELECT * FROM patients WHERE phone = '{phone_no}'"
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            elif choice == 6:
                sql_query = f"SELECT * FROM patients WHERE gender = 'male'"
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif choice == 7:
                sql_query = f"SELECT * FROM patients WHERE gender = 'female'"
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             
            elif choice == 8:
                sql_query = 'SELECT * FROM patients ORDER BY created_on'
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif choice == 0:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Patient Menu Closing...')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
            else:
                print("Invalid choice")


    def show_consultation_menu(self):
        while True:
            print("1. Add new consultation")
            print("2. Update Existing consultation")
            print("3. Delete Existing consultation")
            print("4. Fetch All Existing consultation")
            print("5. Fetch consultation by Patient")
            print("0. Quit")            
            choice = int(input('Enter you choice: '))
            if choice == 1:

                ans = input('do you know the patient id? (Y/N)\n').lower()
                if ans == 'y':
                    p_id = int(input("Enter Patient ID for consultation: "))
                else:
                    phone_number = input('Enter the phone number: ')
                    sql_query = f"select * from patients where phone={phone_number}"
                    rows = self.db_helper.read(sql_query)
                    if len(rows)==1:
                        p_id = rows[0][0]
                        print(f'patient id is {rows[0][0]}, and the name is {rows[0][1]}')



                consultation = Consultation()
                consultation.input_consultation()
                consultation.p_id = p_id

                sql_query = f"INSERT INTO consulation VALUES(null, {consultation.p_id},'{consultation.remarks}','{consultation.medicine}','{consultation.followup}','{consultation.created_on}');"
                self.db_helper.write(sql_query)
            elif choice == 2:
                pass
            elif choice == 3:
                c_id = int(input("Enter the Consultation id to delete: "))
                sql_query = f"delete from consulation where c_id={c_id}"
                self.db_helper.write(sql_query)

            elif choice == 4:
                sql_query = 'select * from consulation'
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                

            elif choice == 5:
                p_id = input("Enter the patient id to show: ")
                sql_query = 'select * from consulation where p_id = {}'.format(p_id)
                rows = self.db_helper.read(sql_query)
                if len(rows)==0:
                    print("No consultation found for this patient")
                    
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                    for row in rows:
                        print(row)

                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            elif choice == 0:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Patient Menu Closing...')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
            else:
                print("Invalid choice")

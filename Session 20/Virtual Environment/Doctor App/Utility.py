# view + controller
import datetime
from DBhelper import DBhelper
from Patient import Patient


class DoctorsApp:
    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('Welcome to doctors app')
        print('App stated at',datetime.datetime.now())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        self.db_helper = DBhelper()


    def show_main_menu(self):
        while True:
            print("1. For Patient")
            print("2. For Consultation")
            print("3. Quit")
            choice = int(input('Enter you choice: '))
            if choice == 1:
                self.show_patient_menu()
            elif choice == 2:
                self.show_consultation_menu()
            elif choice == 3:
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
            print("8. Quit")
            choice = int(input('Enter you choice: '))
            if choice == 1:
                patient = Patient()
                patient.input_patient()

                sql_query = f"INSERT INTO patients VALUES(NULL, '{patient.name}', '{patient.phone}', '{patient.email}', '{patient.dob}', '{patient.gender}', '{patient.created_on}')"
                self.db_helper.write(sql_query)

            elif choice == 2:
                pass
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
                sql_query = f"SELECT * FROM patients WHERE gender = 'mail'"
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif choice == 7:
                sql_query = f"SELECT * FROM patients WHERE gender = 'femail'"
                rows = self.db_helper.read(sql_query)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                for row in rows:
                    print(row)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif choice == 8:
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
            print("6. Quit")            
            choice = int(input('Enter you choice: '))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Patient Menu Closing...')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
            else:
                print("Invalid choice")

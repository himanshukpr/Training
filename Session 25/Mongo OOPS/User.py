import datetime
import hashlib

class User:
    def __init__(self, name=None, age=None, phone=None, email=None,address=None, gender=None):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address
        self.gender = gender
        self.created_on = datetime.datetime.now()
        
        print('User object created')

    def input_user_details(self):
            errors = []
            re_enter = ['name', 'age', 'email', 'phone', 'address','gender','password']
            while True:
                errors.clear()

                if 'name' in re_enter:
                    self.name = input('Enter name: ')
                    if len(self.name) == 0:
                        errors.append('[Error] Name cannot be empty')
                        # re_enter.append('name')
                    else:
                        if 'name' in re_enter:
                            re_enter.remove('name')

                if 'age' in re_enter:
                    self.age = int(input('Enter age: '))
                    if self.age < 15:
                        errors.append('[Error] Age is not valid')
                        # re_enter.append('age')
                    else:
                        if 'age' in re_enter:
                            re_enter.remove('age')
                
                if 'email' in re_enter:
                    self.email = input('Enter email: ')
                    if len(self.email) == 0:
                        errors.append('[Error] email cannot be empty')
                        # re_enter.append('email')
                    elif '@' not in self.email or '.' not in self.email:
                        errors.append('[Error] email is not valid')
                        # re_enter.append('email')
                    else:
                        if 'email' in re_enter:
                            re_enter.remove('email')

                
                if 'phone' in re_enter:
                    self.phone = input('Enter phone: ')
                    if len(self.phone) != 10:
                        errors.append('[Error] phone no must be 10 digits')
                        # re_enter.append('phone')
                    else:
                        if 'phone' in re_enter:
                            re_enter.remove('phone')

                if 'address' in re_enter:
                    self.address = input('Enter address: ')
                    if len(self.address) == 0:
                        errors.append('[Error] address cannot be empty')
                        # re_enter.append('address')
                    else:
                        if 'address' in re_enter:
                            re_enter.remove('address')


                if 'gender' in re_enter:
                    self.gender = input('Enter gender: ')
                    if len(self.gender) == 0:
                        errors.append('[Error] gender cannot be empty')
                        # re_enter.append('gender')
                    else:
                        if 'gender' in re_enter:
                            re_enter.remove('gender')

                if 'password' in re_enter:
                    self.password = input('Enter password: ').encode('utf-8')
                    
                    if len(self.password) < 6:
                        errors.append('[Error] password must be minimam 6 characters long')
                    else:
                        self.password = hashlib.sha256(self.password).hexdigest()
                        if 'password' in re_enter:
                            re_enter.remove('password')


                if len(errors) != 0:
                    print('Errors found:')
                    for error in errors:
                        print(error)
                    print('Please re-enter the details')
                else:
                    break


    def show(self):
        print(f"~~~~~~~~~~~~~~~~{self.name}~~~~~~~~~~~~~~~~~~~~~")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"gender: {self.gender}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def to_document(self):
        return vars(self)
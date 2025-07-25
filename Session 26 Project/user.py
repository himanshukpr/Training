import datetime

class User:
    def __init__(self, name='', age=0, phone='', email='' ,address='', gender='',password=''):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
        self.gender = gender

        self.created_on = datetime.datetime.now()
        
        print('User object created')


    def show(self):
        print(f"~~~~~~~~~~~~~~~~{self.name}~~~~~~~~~~~~~~~~~~~~~")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"gender: {self.gender}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def to_document(self):
        return vars(self)
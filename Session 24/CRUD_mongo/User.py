class User:
    def __init__(self, name=None, age=None, email=None):
        self.name = name
        self.age = age
        self.email = email
        print('User object created')

    def input_user_details(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.email = input("Enter your email: ")

    def show(self):
        print(f"~~~~~~~~~~~~~~~~{self.name}~~~~~~~~~~~~~~~~~~~~~")
        print(f"Age: {self.age} | Email: {self.email}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def to_document(self):
        return vars(self)
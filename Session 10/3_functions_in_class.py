class User:
    def __init__(self,username, email, phone_no,gender):
        self.username = username
        self.email = email
        self.phone_no = phone_no
        self.gender = gender

    def show(self):
        print("Username: ", self.username)
        print('email:', self.email)
        print('phone no:', self.phone_no)
        print('gender:',self.gender)

john = User('john','john@gmail.com',9865876512,'Male')
john.show()
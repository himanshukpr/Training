class User:
    def __init__(self, name, phone_no, email, wallet, library = None):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.wallet = wallet
        self.library = library

    def show(self):
        print("Name:",self.name)
        print("Phone_no:",self.phone_no)
        print("Email:",self.email)
        print("Wallet:",self.wallet)
        self.library.show()


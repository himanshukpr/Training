import datetime

class Patient:
    def __init__(self, name, phone, email, address, gender, age, doctor_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age
        self.doctor_id = doctor_id
        self.created_at = datetime.datetime.now()

    def to_document(self):
        return vars(self)
    

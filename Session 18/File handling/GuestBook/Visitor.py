"""
Think of object
    name
    purpose
    whom to meet
    date
"""

class Visitor:
    def __init__(self, name=None, purpose=None, whom_to_meet=None, date=None):
        self.name = name
        self.purpose = purpose
        self.whom_to_meet = whom_to_meet
        self.date = date

    def add(self):
        self.name = input("Enter your name: ")
        self.purpose = input("Enter the purpose of your visit: ")
        self.whom_to_meet = input("Enter the name of the person you want to meet: ")
        self.date = input("Enter the date of your visit (DD/MM/YYYY): ")

    def csv(self):
        return '{}, {}, {}, {}'.format(self.name, self.purpose, self.whom_to_meet, self.date)

    def __str__(self):
        return f"Name: {self.name}, Purpose: {self.purpose}, Whom to meet: {self.whom_to_meet}, Date: {self.date}"
    


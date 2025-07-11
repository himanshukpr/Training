'''
    module in python
        a program i.e a file that contains python code
        some logic is refered to as a module

        >> a python program is a module
'''

"""
    think of the class
        Visitor Book Library = date time, name, roll no, branch, purpose
"""
import datetime
class Visitor:
    def __init__(self, date_time=None, name=None, roll_no=None, branch=None, purpose=None):
        self.date_time = date_time
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.purpose = purpose
        

    def add_visitor(self):
        self.date_time = datetime.datetime.now()
        self.name = input('Enter your Name: ')
        self.roll_no = input('Enter you Roll No: ')
        self.branch = input("Enter you Branch:")
        self.purpose = input("Enter you Purpose: ")


    def __str__(self):
        return "{},{},{},{},{},{}".format(self.srno, self.date_time, self.name, self.roll_no, self.branch, self.purpose)

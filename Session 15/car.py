class Car:
    def __init__(self, name='', color=''):
        self.name = name
        self.color = color
        self.next = None
        self.previous = None
    
    def __str__(self): # BY USING THIS WE DON'T NEED TO USE THE SEPERATE DISPLAY OR SHOW FUNCTION IN THE CLASS
        return f"""
-----------------------------
car name {self.name} 
color {self.color}
-----------------------------
"""
    
    def car_input(self):
        self.name = input('Enter the car Name: ')
        self.color = input('Enter the color name: ')

    
    def user_input(self):
        self.name = input('Enter the car Name: ')
        self.color = input('Enter the color name: ')

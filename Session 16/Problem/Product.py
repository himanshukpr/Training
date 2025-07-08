class Product_info:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.next = None
        self.previous = None
    
    def __str__(self): # BY USING THIS WE DON'T NEED TO USE THE SEPERATE DISPLAY OR SHOW FUNCTION IN THE CLASS
        return f"""{self.name} ------ {self.price} ------ {self.quantity}"""
        

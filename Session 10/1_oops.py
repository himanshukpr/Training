"""
oops has two types of the relationships
- HAS-A
    - restaurant has 1 menu (two object may me related)
    - 1 menu has many dishes
    - many restaurants has many dishes

- IS-A
    - inheritance 
"""

"""
requirement - 
client wants to create the application to buy the product online from any where
    one can create the account in this
     - create user,login, username, phone no, email, address etc
    deliveryAgent
     - username, phone no, email, address, rating, address etc

the application contains many categorys of the product and
user can place the order for any particular type of the product
all the particular product contains the particular information just like the image or the name etc

"""


'''
step 1 creating the object
objects - 
    user - create user,login, username, phone no, email, address etc
    deliveryAgent - create user,login, username, phone no, email, address etc
    Categories - type, products
    products - name, description, price, images, rating, reviews, category, stock etc
    order - location, destination, product, deliveryAgent, duration, delivery type, feedback etc

'''

# user - create user,login, username, phone no, email, address etc

# creating the representation of the object (i.e class)
class User:
    # in python __init__ function is the constructor 
    # not like other language.
    # self is an input to the constructor (i.e an argument)
    # sefl will have the hashcode of the class
    def __init__(self):
        print("constructor executed")
        print('self: ', self,type(self),id(self))

# step 3 creating the object in the memory
# object construction statement
# creating the object from the class
# sia is the refernce variable and this will hold the hashcode of the object
sia = User()
print("sia user:",sia, type(sia), id(sia)) 
# the output is exactly same


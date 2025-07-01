# in this code we are directly passing the objects to other objects without using the reference variables

from has_a_game1 import Game
from has_a_library2 import Library
from has_a_user3 import User


# using the following the data will not be remain in the heap
user = User(name="John",
            phone_no=896598632,
            email='john@gmail.com',
            wallet=450,
            library=Library(games=[
                            Game(name='God of war',price=3799,rating=4.7),
                            Game(name = 'COD', price=1599, rating=4.2),
                            Game(name = 'Battlefield', price=2599, rating=4.1)
                        ])).show()
"""
# using the following the data will be remain in the heap
user = User(name="John",
            phone_no=896598632,
            email='john@gmail.com',
            wallet=450,
            library=Library(games=[
                            Game(name='God of war',price=3799,rating=4.7),
                            Game(name = 'COD', price=1599, rating=4.2),
                            Game(name = 'Battlefield', price=2599, rating=4.1)
                        ]))
user.show()
"""
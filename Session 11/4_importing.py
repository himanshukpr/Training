from has_a_game1 import Game
from has_a_library2 import Library
from has_a_user3 import User

game1 = Game(name='God of war',price=3799,rating=4.7)
game2 = Game(name = 'COD', price=1599, rating=4.2)
game3 = Game(name = 'Battlefield', price=2599, rating=4.1)

# list of the game
#         0       1     2
games = [game1, game2, game3]

library = Library(games=games) # 1 to many realtionship: one library has many games 

user = User(name="John",
            phone_no=896598632,
            email='john@gmail.com',
            wallet=450,
            library=library) # this is called the 1 : 1 mapping



user.show()
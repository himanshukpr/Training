"""
    oops
        has-a relationshipt between objects
        there is a application that allows other to buy and play the games over the network without even downloading that game
        for this the following things are required
        user - a user can has only one library
        library - library may contain many games


        object  |  attributes
        ---------------------------------------------------------------
        user    |   user_id, name, phone_no, email, wallet
        library |   games, number_of_games
        game    |   name, price, rating

"""
"""
    user - a user can has only one library
    library - library may contain many games

"""



class Game:
    def __init__(self,name = 'NA', price=0, rating=0):
        # LHS self.name -> in the object we will create an attribute name
        # RHS name (this is the input whch we can pass in the constaructor as value)
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print('------------------Game---------------------')
        print("Name:",self.name)
        print("Price:",self.price)
        print("Rating:",self.rating)
        print('---------------------------------------')


        
'''
# LHS : refernce variable that holds the hashcode of the object
# RHS : 'Game()' execution of the constructor with default and the custom values
game1 = Game()
game2 = Game(name = 'COD', price=1599, rating=4.2)
game3 = Game(name = 'Battlefield', price=2599, rating=4.1)


print(game1)
print(game2)
print(game3)

game1.show()
game2.show()
game3.show()
'''
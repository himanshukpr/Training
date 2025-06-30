
class Song:
    def __init__(self):
        print("constructor executed")
        print('self: ', self,type(self),id(self))


john = Song()
print(john, type(john),id(john))

john.name = 'ishq risk'
john.artist = 'Rahat Fateh Ali Khan'
john.album = 'Mere Brother Ki Dulhan'
john.duration = '4.12'
# update operation
john.duration = '4.32'
# delete operation
del john.duration


print(vars(john)) # this will show the dictionary of the object variables

# reference copy operation
jonnie = john # here the both object is same i.e the hashcode is same

print(vars(jonnie))
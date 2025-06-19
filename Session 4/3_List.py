names = ['himanshu','raj','john']
followers = names
print("Names: ",names, type(names), id(names))
print("Followers: ",followers, type(followers), id(followers))
print("~~~~~~~~~~~~~~~~~~~~")


names = ['rohit','raj','john'] # this will create a new list in the HEAP memor
names[0] = 'george'

print("Names: ",names, type(names), id(names))
print("Followers: ",followers, type(followers), id(followers))

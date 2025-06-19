names = ['himanshu','raj','john']

print(names, type(names), id(names))
print("Names: ",names[1], type(names[1]), id(names[1]))

print("~~~~~~~~~~~~~~~~~~~~")
names.append('rohit')


followers = names
followers[1] = "jatin"

print("Names: ",names, type(names), id(names))
print("Names: ",names[1], type(names[1]), id(names[1]))
print("~~~~~~~~~~~~~~~~~~~~")
print("Followers: ",followers, type(followers), id(followers))

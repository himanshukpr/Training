# Use of the List
followers = ['John', 'Paul', 'George', 'Ringo','John']# this will allow duplicates

print(followers)

followers = {'John', 'Paul', 'George', 'Ringo','John'} # this will not allow duplicates

john_followers = {'Paul', 'Ringo','Sia', 'Jennie'}


# mutual_followers = followers.intersection(john_followers)
mutual_followers = followers & john_followers
print(followers)
print(john_followers)

# for loop : Enhaced version of the for loop, for each loop
for name in mutual_followers:
    print(name)
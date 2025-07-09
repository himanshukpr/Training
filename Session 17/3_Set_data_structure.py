john_followers = {"Alice", "Bob", "Charlie", "David", "Eve","Bob"}
print("John's followers:", john_followers)
print("type(john_followers)", type(john_followers))
print("len(john_followers):", len(john_followers))

print(min(john_followers))
print(max(john_followers))

data = set(range(10, 101, 10))
print('data',data)
print('sum is:', sum(data))
print('average is:', sum(data)/len(data))


data.add(110)
data.remove(30)
data.pop() # removes an arbitrary element
print('after adding 110:', data)


john_followers = {"Alice", "Bob", "Charlie", "David", "Eve"}
jack_followers = {"Alice", "Bob", "Charlie", "Frank", "Grace"}
fionna_followers = {"Alice", "Bob"}


mutual_followers = john_followers.intersection(jack_followers, fionna_followers)
print("Mutual followers:", mutual_followers)

result = fionna_followers.issubset(john_followers)
print("Is Fionna's followers a subset of John's followers?", result)

result = john_followers.issuperset(fionna_followers)
print("Is John's followers a superset of Fionna's followers?", result)



a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5}

# c = a + b
d = a - b
e = a ^ b
f = a | b

# print(c)
print(d)
print(e)
print(f)
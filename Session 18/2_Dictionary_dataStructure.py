
# ordered dictionary

my_data = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}
print(my_data)

# all utilies functions works on the keys instead of the values
print("len(my_data):",len(my_data))
print("min(my_data):",min(my_data))
print("max(my_data):",max(my_data))
print("sum(my_data):",sum(my_data))

value = my_data[101]
print("my_data[101]:",value)

print('data', my_data.get(101))  # Using get method to access value


# update:
my_data[101] = "Frank"
print(my_data)

# delete:
my_data.pop(101)
del my_data[102]
print(my_data)

# adding new key-value pair:
my_data[106] = "Grace"
print(my_data)




'''
my_data = {
    'john': 25,
    'jane': 30,
    'doe': 22,
    'alice': 28,
    'bob': 35
}
print("len(my_data):",len(my_data))
print("min(my_data):",min(my_data))
print("max(my_data):",max(my_data))
# print("sum(my_data):",sum(my_data)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
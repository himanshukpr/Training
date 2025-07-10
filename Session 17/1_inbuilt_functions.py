'''
    single value container ( which can hold only 1 value)
    int, float, bool

    multi value containers ( which can hold lot of data)
    objects -> tuple, list , string, set dictionary

    sequences
        tuple
        list
        string

        storage of the data in sequential or liner

    set & dictionary
        storage of the data is non sequential or non linear


    properties:
    1. Indexing
    2. Negatice indexing
    3. Slicing
    4. Concatenation
    5. multiplicity
    6. Mumbership testing



'''
'''
# list or set
# 1-D list
my_data = [10,20,30,40]

print(my_data[0])
print(my_data[-1])
print(len(my_data))

# list of list
# 2-D list - container contains another container
numbers = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(numbers[0][1])
'''


"""
# nagative indexing
name = 'john\'s cafe'
message = '''alot of content in the same string'''

print(message)
print(len(message))
print(message[0])
print(message[-1])

"""
"""
# slicing or subset
data = list(range(10,101,10))

print(data[3 : 7]) # from 3 to 7-1 -> 6
print(data[3 : ])
print(data[ : -4])


email = 'john@example.com'
name = email[:4]
domain = email[5:]

print(name)
print(domain)
"""


# concatenation

data1 = [10,20,30,40]
data2 = [40,50,60]

data3 = data1 + data2
print(data3)



name1 = 'john'
name2 = 'doe'
name3 = name1+' '+name2
print(name3)


# multiplicity
data = [10,20,30]
data2 = data * 3
print(data2)

data = 12,32
data2 = data * 3
print(data2)



# membership testing
data = [10,20,30,40,50]
print("here:",60 not in data)


data = {10,20,30,40,50} # set (tree set)
student = {
    'name': 'john',
    'age': 30,
    'email': 'john@gmail.com'
}
print(10 in data)
print('age' in student)
# following will not work
# print(data[:5])
# data = student[:1]

# print(data[0]) 
# data2 = data * 2
# print(data2)
# data2 = {20,50} + data
# print(data2)

# student2 = student * 2
# print(student2)
# list datastructure
numbers = list(range(10, 101,10))
print('numbers:', numbers)


numbers.append(110)

print('after append:', numbers)
print('length of numbers:', len(numbers))
print('sum of numbers:', sum(numbers))
print('max of numbers:', max(numbers))
print('min of numbers:', min(numbers))
print('average of numbers:', sum(numbers)/len(numbers))
print('index of 30:', numbers.index(30))


numbers.reverse()
print('after reverse:', numbers)

data = tuple(numbers)
print('data:', data)

# def reversed_list(data):
#     reversed_data = []
#     for i in range(len(data)-1, -1, -1):
#         reversed_data.append(data[i])
#     return reversed_data


# reversed_numbers = reversed_list(numbers)
# print('reversed numbers:', reversed_numbers)



def reversed_list(data):
    data.reverse()

numbers = [10,20,30,40,50,60,70,80,90,100]
reversed_list(numbers)
print('reversed numbers:', numbers)




numbers.sort()

numbers.remove(30)
print('after removing 30:', numbers)

numbers.clear()

print('after clearing:', numbers)
data = [10, 20, 30, 40]
data.insert(2, 2)
print('after inserting 5 at index 0:', data)
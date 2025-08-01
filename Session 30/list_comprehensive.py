numbers = [10, 11, 30, 40, 50]
my_numbers = [ 'even' if num%2 == 0 else 'odd' for num in numbers]

print(my_numbers)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = [
    *[x**2 for x in list1],
    *[x**2 for x in list2]
]

print(list3)
'''
    search
    time complexity = 0(n)
    linear search
        1. simple list
        2. list of the dictionary
        3. list of the objects
        4. our linked list
'''

def search(data=[], target=None):
    index = 0
    found = False
    while index < len(names):
        if names[index] == name:
            print(f'found at {index} index')
            found = True
            break
        index += 1

    if not found:
        print('not found')


# the sorting must be performed on the homegenous data
data = [10,20,30,40,50]
names = ['john','jennie','anna','kim', 'ben']


# number = int(input('enter number to search: '))
# found = False
# for n in range(len(data)):
#     if data[n] == number:
#         print(f'found at {n} index')
#         found = True
#         break

# if not found:
#     print('not found')

name = input('enter the name to search: ')

search(names,name)


# name  = input("enter you name: ")
# person_to_meet = input("Enter the name of the person you want to  meet: ")
# purpose = input("enter the your purpose of meeting: ")


# print(f"Hello {name}, you want to meet {person_to_meet} for {purpose}.")

# # PERSISTENCE : to save the data permanently from primary source to secondary source.


# file Handling
# we can open the files such as text files, csv files, json files, etc.


# to read a file, we need to open it in read mode.
# file = open('test.txt', 'r')
# data = file.readlines()
# # print(data)
# for line in data:
#     print(line.strip())
# file.close()

with open('test.txt', 'r') as file:
    data = file.read()
    print(data)



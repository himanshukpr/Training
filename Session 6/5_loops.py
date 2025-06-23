user_name = ["John", "Jane", "Jack", "Jill"]

search = input("Enter your name: ")
flag = False
for index in range(4):
    if search == user_name[index]:
        print(search,"Found in the list!")
        flag = True
        break

if flag == False:
    print(search,"Not found")


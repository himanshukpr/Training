user_name = ["John", "Jane", "Jack", "Jill"]

search = input("Enter your name: ")

# for name in user_name:
#     if search == name:
#         print("User Found", search)
#         break
# else:
#     print(search,"not found")


# liner search algorithum

inx = 4
i = 0
flag = False
while i < inx:
    if search == user_name[i]:
        print("User Found", search, "at index", i)
        flag = True
        break
    i += 1

if flag == False:
    print(search,"not found")
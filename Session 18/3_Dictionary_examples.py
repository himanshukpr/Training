
# how to create a dictionary with the list, having the keys
months_list = ['january', 'february', 'march', 'april', 'may', 
              'june', 'july', 'august', 'september', 'october', 
              'november', 'december']

college_attendance = {}.fromkeys(months_list, 100)

college_attendance['january'] -= 10
# print(college_attendance)



students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']



attendance = {}.fromkeys(students, {}.fromkeys(months_list, 100))

print(attendance)
from Visitor import Visitor


visitor = Visitor()
visitor.add()


with open('guestbook.csv','a+') as file:
    if len(file.read()) == 0:
        file.write('Name,Purpose,Person to meet,Date\n')  # Write header if file is empty
    file.write(visitor.csv() + '\n')
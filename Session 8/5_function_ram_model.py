def square(number):
    print("1. number is:", number, id(number))
    number = number * number # it will create the new container and the number will refer to that container
    print("2. number is:", number, id(number))

# in this a new variable is created but it will copy the reference from the main

number = 10
print('3. number is ', number, id(number))
square(number)
print('4. number is', number, id(number))
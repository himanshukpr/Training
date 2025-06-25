def square(numbers):
    print("[square] number is:", numbers, id(numbers))

    for i in range(len(numbers)):
        print("[square]", i, numbers[i], id(numbers[i]))

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]

    print("[square] number is:", numbers, id(numbers))
    

    for i in range(len(numbers)):
        print("[square]", i, numbers[i], id(numbers[i]))

# in this a new variable is created but it will copy the reference from the main

data = [10,20,30,40]
print('3. number is ', data, id(data))
for i in range(len(data)):
    print("[main]", i, data[i], id(data[i]))

square(data)


print('----------------------------')
print('4. number is ', data, id(data))

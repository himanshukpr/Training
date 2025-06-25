def sq(number):
    return number**2

print('square function is',sq)
# print('hashcode is :', id(sq))
# print('hashcode is :', hex(id(sq)))
# print('type is :', type(sq))


# whenever we re-define an existing function
# that time it will remove the old function and will create the new function in the memory
def sq(number1, number2):
    result = [number1**2, number2**2]
    return result

print('now sq is:',sq)
print(sq(5, 6))
# print(sq(10)) # here we will get an error of missing argument -> as old function doesn't exist
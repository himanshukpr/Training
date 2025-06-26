# Default Argument
# you can give default values from left to right
# def add(number1=10, number2): # will give error
def add(number1, number2=10):
    result = number1 + number2
    return result

result_from_add = add(10)
print(result_from_add)
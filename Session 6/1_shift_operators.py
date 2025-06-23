num1 = 8
num2 = 2


result = num1 >> num2 # divide by 2 pow num1
print(result)
result = num1 << num2 # multiply by 2 pow num1
print(result)

data = 8
key = 2
encrypted_data = data >> key
print(encrypted_data)

original_data = encrypted_data << key
print(original_data)


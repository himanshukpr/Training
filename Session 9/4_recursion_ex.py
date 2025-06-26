# def max_num(data):
#     data = data
#     if len(data) == 1:
#         return data[0]
#     elif data[0]>data[1]:
#         data.pop(1)
#         return max_num(data)
#     else:
#         data.pop(0)
#         return max_num(data)
    

# numbers = [10,20,50,30]
# value = max_num(data = numbers)

# print(value)

def max_num(data,length):
    if length == 1:
        return data[0]
    else:
        previous = max_num(data, length-1)
        current = data[length-1]
        if previous > current:
            return previous
        else:
            return current

numbers = [10,20,50]
value = max_num(data = numbers, length = len(numbers))

print(value)


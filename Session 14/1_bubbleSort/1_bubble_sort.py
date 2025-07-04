def sort(value, high_to_low=False):
    if high_to_low == False:
        for i in range(len(value)-1):
            for j in range(len(value)-i-1):
                if value[j] > value[j+1]:
                    temp =  value[j]
                    value[j] = value[j+1]
                    value[j+1] = temp
    else:
        for i in range(len(value)-1):
            for j in range(len(value)-i-1):
                if value[j] < value[j+1]:
                    temp =  value[j]
                    value[j] = value[j+1]
                    value[j+1] = temp
    return value

value = [54,65,34,5,634,23]

names = ["John","Bob","Alice","Joe"]

sort(names)
print(names)
sort(value,high_to_low=True)
print(value)

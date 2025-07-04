# Selection Sort

def selection_sort(data):
    min = 0
    for i in range(len(values)):
        min = i
        for j in range(i,len(values)):
            if values[j] < values[min]:
                min = j
            
        temp = values[i]
        values[i] = values[min]
        values[min] = temp

    return values


values = [n for n in  range(10,0,-1)]

selection_sort(values)
    
print(values)

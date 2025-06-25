def max_number(list):
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    print("--------------------------------")
    print(max)
    print("--------------------------------")



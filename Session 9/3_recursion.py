# sometimes the loops are not able for the dynamic and this is work on the index

# functions - replacing loops
# recursion - executing a function again and again
# execution must stop on some condition


def print_number(number):
    print(number)
    if number>1:
        return print_number(number - 1)

print_number(10)


# functions have total 3 components
# execution will be always sequeantial in functions

# create statement: create function in Memory
def f(a,b): # this is 1st component
    print("2nd component is body") # 2nd components
    print(a)
    print(b)
    c = a + b
    print('result is ',c)
    return c
    # return keyword will always at the end of the function (by default it is NONE)
    # return mean the termination of the function


print("hello") # this is in the main theat, so it will run
print("result from f is",f(a=2,b=5)) # 3rd component of the function
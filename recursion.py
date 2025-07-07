def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n * factorial(n-1)
    
def fibbo(n):
    if n==0 or n==1:
        print(n)
        return()
    else:
        value = fibbo(n-1)+fibbo(n-2)
        print(value)


fibbo(5)
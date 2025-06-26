# Nesting of function
def fun(f):
    print(f)

def hello():
    print("hello")

fun(hello)
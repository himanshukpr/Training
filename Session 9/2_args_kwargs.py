def add(*args): # the args can be anything: *args -> *kuchbhi
    print(args)
    print(id(args))
    print(type(args))
    print(sum(args))

add(2,5,4)


def mul(**kwargs):
    print(kwargs)
    print(id(kwargs))
    print(type(kwargs))
    print(kwargs.values())
    # for value in kwargs:
    #     print(value)

mul(a=10, b=20, c=30)

def user(**kwargs):
    print(kwargs)

user(name="himanshu",email="abc@gmail.com")
def user(**kwargs):
    print(kwargs)

user(name="himanshu",email="abc@gmail.com")
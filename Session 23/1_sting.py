'''
    strings are immuatable
    once, created, cannot be changed

    anytime we modify the string, a new string will be created in the memory
'''

str = 'be EXceptional, work hard'
print(str)

upper_str = str.upper()
print(upper_str)

lower_str = str.lower()
print(lower_str)


print(str.capitalize())
print(str.title())
print(str.swapcase())




password = '    password123 '
print(password) 
print(password.strip()) # will remove the space from front and at the end of the string

data = '0005689'

print(data.lstrip("0"))






name = 'Ishpreet Singh'

for i in range(len(name)):
    if name[i] == ' ':
        print(" ",end="")
        continue
    if i%2==0:
        print('*',end="")
    else:
        print(name[i],end="")
print()


for i in range(len(name)):
    if i<3:
        print(name[i],end="")
    else:
        print('*',end="")


msg = 'no internet'

print(msg.center(50))
print(msg.rjust(50))
print(msg.ljust(50))


quote = 'search the candle, rather than cursing the darkness'

ind1 = quote.find('the')
ind2 = quote.find('dark')
ind3 = quote.rfind('the')

print(ind1,ind2,ind3)

print(quote[ind1:ind1+3])
print(quote[ind2:])





message = 'hello, how are you. i hope you are good'
new_message = message.replace(",","")
new_message = new_message.replace(".","")
words = new_message.split(' ')
print(words)




name = 'leo'
age = 20
email = 'leo@example.com'

user ={
    'name':'leo',
    'age' :20,
    'email' : 'leo@example.com'
}

class User:
    def __init__(self):
        self.name = 'leo'
        self.age = 20
        self.email = 'leo@example.com'

leo = User()
#string formatting

print('name {} age {} email {}'.format(name, age, email))
print('name {1} age {1} email {0}'.format(name, age, email)) # indexing while string formatting
print('name {a} age {b} email {c}'.format(a=name,b= age,c= email)) # keyvalue pair while string formatting
# formatting with map i.e using dictionary
print('name {name} age {age} email {email}'.format_map(user)) 


print('name {name} age {age} email {email}'.format_map(vars(leo))) 



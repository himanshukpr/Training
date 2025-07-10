
quotes = []
quotes.append(input('Enter the quotes: '))

while True:
    data = input('Enter the quotes: ')
    if data.lower() == 'exit()':
        break
    quotes.append(data) 


with open('quotes.txt','a') as file:
    for q in quotes:
        file.write(q + '\n')
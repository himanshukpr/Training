from Book import Book
from Books_stack import Book_stack

book1 = Book("1 book")
book2 = Book("2 book")
book3 = Book("3 book")

books = Book_stack()
books.push(book1)
books.push(book2)
books.push(book3)


books.show()
books.pop()
print('-----------------------------------------------')
books.show()
from Book import Book
from Books_queue import Book_queue

book1 = Book("1 book")
book2 = Book("2 book")
book3 = Book("3 book")

books = Book_queue()
books.enq(book1)
books.enq(book2)
books.enq(book3)


books.show()
books.deq()
print('-----------------------------------------------')
books.show()
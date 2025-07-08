class Book_queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enq(self, book):
        self.size += 1
        if self.head == None:
            self.head = book
            self.tail = book
        else:
            self.tail.next = book
            book.previous = self.tail
            self.tail = book

    def deq(self):
        self.size -= 1
        head = self.head
        self.head.next.previous = None
        self.head = self.head.next
        del head

    def show(self):
        current = self.head
        print(current)
        while current.next != None:
            current = current.next
            print(current)
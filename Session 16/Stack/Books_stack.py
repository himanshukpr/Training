class Book_stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.stack_size = 0

    def push(self, book):
        self.stack_size += 1
        if self.head == None:
            self.head = book
            self.tail = book
        else:
            self.tail.next = book
            book.previous = self.tail
            self.tail = book

    def pop(self):
        self.stack_size -= 1
        tail = self.tail
        self.tail.previous.next = None
        self.tail = self.tail.previous
        del tail

    def show(self):
        current = self.head
        print(current)
        while current.next != None:
            current = current.next
            print(current)
class CarList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, car):
        self.size += 1
        if self.head == None:
            self.head = car
            self.tail = car
        else:
            car.previous = self.tail
            self.tail.next = car
            self.tail = car
            self.head.previous = self.tail
            self.tail.next = self.head

    def show(self):
        current = self.head
        print(current)
        while current.next!=self.head:
            current = current.next
            print(current)

    def delete(self, name):
        current = self.head
        found = False
        print(name)
        while current.next != self.head:
            current = current.next
            if current.name == name:
                current.next.previous = current.previous
                current.previous.next = current.next
                found = True
                print("Delete successful")
                break

        if not found:
            print('car not found')\
                

    def head_delete(self):
        self.head = self.head.next
        self.head.previous = self.tail
        self.tail.next = self.head

    def tail_delete(self):
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail




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

    def show(self):
        current = self.head
        print(current)
        while current.next!=None:
            current = current.next
            print(current)



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
        while current.next != self.head:
            current = current.next
            if current.name == name:
                current.next.previous = current.previous
                current.previous.next = current.next
                found = True
                self.size -= 1
                del current
                print("Delete successful")
                break

        if not found:
            print('car not found')
                

    def head_delete(self):
        self.size -= 1
        head = self.head
        self.head = self.head.next
        self.head.previous = self.tail
        self.tail.next = self.head
        del head


    def tail_delete(self):
        self.size -= 1
        tail = self.tail
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail
        del tail

    def add_in_front(self,car):
        self.size += 1
        car.next = self.head
        car.previous = self.tail
        self.head.previous = car
        self.tail.next = car
        self.head = car


    def add_in_between(self,name,car):
        current = self.head
        found = False
        if current.name == name:
            car.next = current.next
            current.next = car
            car.previous = current.next.previous
            current.next.previous = car
            self.size += 1
            print('car added after',name)

            return
        for i in range(self.size):
            current = current.next
            if current.name == name:
                car.next = current.next
                current.next = car
                car.previous = current.next.previous
                current.next.previous = car
                self.size += 1
                found = True
                print('car added after',name)
                return
            
        if not found:
            print("not Found")
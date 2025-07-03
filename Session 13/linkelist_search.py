class FlightList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, flight):
        self.size += 1
        if self.head == None:
            self.head = flight
            self.tail = flight
        else:
            flight.pre = self.tail
            self.tail.next = flight

            self.tail = flight
            self.tail.next = self.head
            self.head.pre = self.tail
            
    def search(self, target):
        current = self.head
        flag = False

        if current.flight_code == target:
            current.show()
            flag = True

            return
        else:
            while current.next != self.head:
                current = current.next
                if current.flight_code == target:
                    print("Flight Found")
                    current.show()
                    flag = True
                    break

        if flag == False:
            print("Flight not found")

    def filter(self, source, destination):
        current = self.head
        if current.source == source and current.destination == destination:
            current.show()
        while current.next!=self.head:
            current = current.next
            if current.source == source and current.destination == destination:
                current.show()

                

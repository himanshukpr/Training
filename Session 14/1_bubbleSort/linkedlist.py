class Flightlist:
    def __init__(self):
        self.tail = None
        self.head = None
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

    
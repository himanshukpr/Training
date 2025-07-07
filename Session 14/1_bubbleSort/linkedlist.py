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

    def bubble_sort(self):
        for i in range(self.size):
            current = self.head

            for j in range(self.size-i-1):

                current = current.next
                if current.next!=None:

                    if current.fare > current.next.fare:
                        if current.pre!= None:
                            current.next.pre = current.pre
                        else:
                            current.next.pre = None
                            self.head = current.next

                        current.pre = current.next

                        if current.next.next!= None:
                            current.next = current.next.next
                        else:
                            current.next = None
                            self.tail = current


                        current.pre.next = current
                            


     
# def bubble_sort(self):
#     if self.head is None or self.head.next is None:
#         return  # Nothing to sort with 0 or 1 nodes
        
#     for i in range(self.size):
#         current = self.head
        
#         for j in range(self.size - i - 1):
#             if current and current.next and current.fare > current.next.fare:
#                 # Swap nodes
#                 next_node = current.next
                
#                 # Update previous node's next pointer
#                 if current.pre:
#                     current.pre.next = next_node
#                 else:
#                     self.head = next_node
                
#                 # Update next_node's next node's previous pointer
#                 if next_node.next:
#                     next_node.next.pre = current
                
#                 # Update current's pointers
#                 current.next = next_node.next
                
#                 # Update next_node's pointers
#                 next_node.pre = current.pre
#                 next_node.next = current
#                 current.pre = next_node
                
#                 # If we just moved the tail, update it
#                 if current.next is None:
#                     self.tail = current
#             else:
#                 # Move to next node if no swap happened
#                 current = current.next




    def show(self):
        current = self.head
        current.show()
        while current.next != None:
            current  = current.next
            current.show()


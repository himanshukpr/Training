class Cart:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.total_amount = 0

    def add(self, product):
        self.size += 1
        if self.head == None:
            self.head = product
            self.tail = product
        else:
            product.previous = self.tail
            self.tail.next = product
            self.tail = product
            self.head.previous = self.tail
            self.tail.next = self.head

    def show(self):
        current = self.head
        print(current)
        while current.next!=self.head:
            current = current.next
            print(current)

    def delete(self, name):
        if name == self.head.name:
            self.head_delete()
            return
        elif name == self.tail.name:
            self.tail_delete()
            return

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
            print('product not found')
                

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

    def add_in_front(self,product):
        self.size += 1
        product.next = self.head
        product.previous = self.tail
        self.head.previous = product
        self.tail.next = product
        self.head = product

    def update_quantity(self,name, quantity):
    
        current = self.head
        found = False
        if current.name == name:
            # print('Found',current)
            current.quntity = quantity
            found = True
        else:
            while current.next !=self.head:
                current = current.next
                if current.name == name:
                    # print('Found',current)
                    current.quntity = quantity
                    found = True
                    break

        if not found:
            print('not found')
            return
        
        if quantity == 0:
            print("deleting")
            self.delete(name=name)
        else:
            current.quantity = quantity



    def search(self, name):
        current = self.head
        found = False
        if current.name == name:
            print('Found',current)
            found = True
        else:
            while current.next !=self.head:
                current = current.next
                if current.name == name:
                    print('Found',current)
                    found = True
                    break

        if not found:
            print('not found')
            return
        
    def discount(self,promo_code):
        current = self.head
            
        self.total_amount += current.price
        while current.next != self.head:
            current = current.next
            self.total_amount += current.price

        if promo_code == "BUY20":
            discount = self.total_amount - (self.total_amount*0.2)
            print(f"total is {self.total_amount} and after 20% balance is {discount}")
        else:
            print(f"Code is invalid. pay {self.total_amount} to continue")
            



    def sort(self):
        print('sorting')
        def swap_node(a,b):
            pre = a.pervious
            next = b.next

            pre.next = b
            b.previous = pre

            b.next = a
            a.previous = b

            a.next = next
            next.previous = a

            if self.head == a:
                self.head = b
            if self.tail == b:
                self.tail = a

            # prev = a.previous
            # next = b.next

            # prev.next = b
            # b.previous = prev

            # b.next = a
            # a.previous = b

            # a.next = next
            # next.previous = a

            # # Update head and tail if needed
            # if self.head == a:
            #     self.head = b
            # if self.tail == b:
            #     self.tail = a



            for i in range(self.size):
                current = self.head
                for j in range(self.size-i-1):
                    if current.price > current.next.price:
                        swap(current,current.next)
                    else:
                        current = current.next

    # def sort(self):
        def swap_nodes(a, b):
            # Swap two adjacent nodes a and b where b = a.next
            prev = a.previous
            next = b.next

            prev.next = b
            b.previous = prev

            b.next = a
            a.previous = b

            a.next = next
            next.previous = a

            # Update head and tail if needed
            if self.head == a:
                self.head = b
            if self.tail == b:
                self.tail = a

        for i in range(self.size):
            current = self.head
            for j in range(self.size - i - 1):
                if current.price > current.next.price:
                    swap_nodes(current, current.next)
                    # After swapping, current still points to the first node in the pair,
                    # so move current to next node to continue
                    # current = current.previous
                else:
                    current = current.next
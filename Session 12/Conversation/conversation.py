class Conversation:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, chat):
        self.size += 1
        if self.head == None:
            self.head = chat
            self.tail = chat
        else:
            chat.previous = self.tail
            self.tail.next = chat
            self.tail = chat

class Chat:
    def __init__(self, message=None):
        self.message = message
        self.previous = None
        self.next = None

    def show(self):
        if not self.previous:
            print("No previous message")
        else:
            print(self.previous.message)

        print('--------------------------------------------')
        print(self.message)
        print('--------------------------------------------')
        if not self.next:
            print("No next message")
        else:
            print(self.next.message)


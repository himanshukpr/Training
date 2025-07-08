class Book:
    def __init__(self,name):
        self.name = name
        self.next = None
        self.previous = None

    def __str__(self):
        return f"""Book name {self.name}"""

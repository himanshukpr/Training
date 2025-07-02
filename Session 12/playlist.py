# circular doubly linked list (dynamic)

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

# add is goind to add a song
    def add(self, song):
        self.size += 1

        if self.head == None:
            self.head = song
            self.tail = song
        else:
            self.tail.next = song
            song.previous = self.tail
            self.tail = song
            song.next = self.head
            self.head.previous = song

    def show(self):
        current = self.head
        print("Playlist")
        print('Total Songs',self.size)

        while True:
            print(current.track)
            current = current.next
            if current == self.head:
                break


        

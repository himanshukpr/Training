
class Song:
    def __init__(self, track='NA', artist='NA', album='NA', duration=0):
        self.track = track
        self.artist = artist
        self.album = album
        self.duration = duration
        self.next = None
        self.previous = None


    def last(self):
        print(self.previous.track)

    def show(self):
    
        print("--------------------------------")
        print("~~~~~~~~~~~preivous~~~~~~~~~~~~~")
        print(self.previous.track)        
        print("~~~~~~~~~~~current~~~~~~~~~~~~~")
        print(f" {self.track}")
        print(f"Artist: {self.artist}")
        print(f"Album: {self.album}")
        print(f"Duration: {self.duration}")
        print("~~~~~~~~~~~next~~~~~~~~~~~~~")
        print(self.next.track)
        print("--------------------------------")

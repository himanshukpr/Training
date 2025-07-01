"""
    1. song : track, artist, album, duration

"""

class Song:
    def __init__(self, track, artist, album, duration):
        self.track = track
        self.artist = artist
        self.album = album
        self.duration = duration
        self.next = None
        self.privous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Track: {self.track}")
        print(f"Artist: {self.artist}")
        print(f"Album: {self.album}")
        print(f"Duration: {self.duration}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")


song1 = Song(track='song1', artist='artist1', album='album1', duration='duration1')
song2 = Song(track='song2', artist='artist2', album='album2', duration='duration2')
song3 = Song(track='song3', artist='artist3', album='album3', duration='duration3')

song1.next = song2
song2.next = song3
song3.next = song1

song1.privous = song3
song2.privous = song1
song3.privous = song2

song1.show()
song2.show()
song3.show()
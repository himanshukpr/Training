from song import Song
from playlist import Playlist

song1 = Song(
    track='1. Laal Pari (From "Housefull 5")',
    artist='Yo Yo Honey Singh, Simar Kaur, Alfaaz',
    album='Laal Pari (From "Housefull 5")',
    duration=4.16
)

song2 = Song(
    track='2. Zamaana Lage (From "Metro ... In Dino")',
    artist='Pritam, Arijit Singh, Shashwat Singh, Qaisar Ul Jafri, SANDEEP SRIVASTAVA',
    album='Zamaana Lage (From "Metro ... In Dino")',
    duration=3.16
)

song3 = Song(
    track='3. Chor Bazari Phir Se (From "Bhool Chuk Maaf")',
    artist='Tanishk Bagchi, Pritam, Irshad Kamil, Sunidhi Chauhan, Neeraj Sridhar, Zahrah S Khan',
    album='Chor Bazari Phir Se (From "Bhool Chuk Maaf")',
    duration=3.01
)
song4 = Song(
    track='4. Koi Naa (From "Bhool Chuk Maaf")',
    artist='Tanishk Bagchi, Gifty, Harnoor, Shreya Ghoshal, Irshad Kamil',
    album='Koi Naa (From "Bhool Chuk Maaf")',
    duration=3.41
)


print(song1)
song_playlist = Playlist()
song_playlist.add(song=song1)
song_playlist.add(song=song2)
song_playlist.add(song=song3)
song_playlist.add(song=song4)

song1.show()
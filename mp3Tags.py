from mutagen.id3 import ID3
from mutagen.mp3 import MP3

song_location = 'bws.mp3'
audio = ID3(song_location)
title = audio['TIT2'].text[0]
artist = audio['TPE1'].text[0]
album = audio['TALB'].text[0]

print(str(title) + ',' + str(audio) + ',' + str(album))
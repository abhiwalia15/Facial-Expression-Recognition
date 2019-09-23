import spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


client_id = '21f99642339d4aa5a5d9199bc60e8bf2'
client_secret = '578a8282d52541e1acc2087e024d8698'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

name = "Coldplay" #chosen artist

result = sp.search(name) #search query
#print(result['tracks']['items'][0]['artists'])

#Extract Artist's uri
artist_uri = result['tracks']['items'][0]['artists'][0]['uri']

#Pull all of the artist's albums
sp_albums = sp.artist_albums(artist_uri, album_type='album')

#Store artist's albums' names' and uris in separate lists

album_names = []
album_uris = []

for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])
    
print(album_names[0])
print(album_uris[0])
#Keep names and uris in same order to keep track of duplicate albums
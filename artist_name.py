import spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


client_id = '21f99642339d4aa5a5d9199bc60e8bf2'
client_secret = '578a8282d52541e1acc2087e024d8698'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
name = "Coldplay" #chosen artist
result = sp.search(name) #search query
print(result['tracks']['items'][0]['artists'])
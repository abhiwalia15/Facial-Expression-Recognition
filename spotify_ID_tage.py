import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Make your own Spotify app at https://beta.developer.spotify.com/dashboard/applications
client_id = '21f99642339d4aa5a5d9199bc60e8bf2'
client_secret = '578a8282d52541e1acc2087e024d8698'
title = 'Juice'
artist = 'Summer Party'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
search_querry = title + ' ' + artist
result = sp.search(search_querry)
for i in result['tracks']['items']:
    # Find a songh that matches title and artist
    if (i['artists'][0]['name'] == artist) and (i['name'] == title):
        print (i['uri'])
        break
else:
    try:
        # Just take the first song returned by the search (might be named differently)
        print (result['tracks']['items'][0]['uri'])
    except:
        # No results for artist and title
        print ("Cannot Find URI")
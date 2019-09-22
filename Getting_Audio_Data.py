import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Make your own Spotify app at https://beta.developer.spotify.com/dashboard/applications
client_id = '21f99642339d4aa5a5d9199bc60e8bf2'
client_secret = '578a8282d52541e1acc2087e024d8698'

uri = 'spotify:track:1V4TCSBKvHpDI41zh60d8J'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
features = sp.audio_features(uri)
print ('Energy:', features[0]['energy'])
print ('Valence:', features[0]['valence'])
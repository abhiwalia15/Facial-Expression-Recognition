import spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


client_id = '21f99642339d4aa5a5d9199bc60e8bf2'
client_secret = '578a8282d52541e1acc2087e024d8698'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

name = "Imagine Dragons" #chosen artist

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
    
print(album_names[5:7])
print(album_uris[5:7])
#Keep names and uris in same order to keep track of duplicate albums

#print(uri)
def albumSongs(uri):
    album = uri #assign album uri to a_name
    spotify_albums[album] = {} #Creates dictionary for that specific album

    #Create keys-values of empty lists inside nested dictionary for album
    spotify_albums[album]['album'] = [] #create empty list
    spotify_albums[album]['track_number'] = []
    spotify_albums[album]['id'] = []
    spotify_albums[album]['name'] = []
    spotify_albums[album]['uri'] = []

    tracks = sp.album_tracks(album) #pull data on album tracks

    for n in range(len(tracks['items'])): #for each song track
        spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
        spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])
        

#albumSongs(album_uris)




spotify_albums = {}
album_count = 0
for i in album_uris[5:7]: #each album
    albumSongs(i)
    print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
    album_count+=1 #Updates album count once all tracks have been added

#print(spotify_albums)


for k, v in spotify_albums.items():
    names = v['name'] 
    #print(names)
    for na in names:
        print(na)

# for key, values in spotify_albums:
#     print(key + ',' + values)
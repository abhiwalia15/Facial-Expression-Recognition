# *************************************************************
# *******************************************************
# *************************************************
# ******************************************


# ********************PART1*****************************
# ***************************************************
# *************************************************

#*************WE ARE IDENTIFYING emotions**********
# ************OF A PERSON IN REAL TIME************
# *********************************************


import os
import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

#load model
model = model_from_json(open("fer.json", "r").read())
#load weights
model.load_weights('fer.h5')


face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
    
    #pre = []

    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)
        roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
        roi_gray=cv2.resize(roi_gray,(48,48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        #find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]
        
        #pre.append(predicted_emotion)
        #print(predicted_emotion)


        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial emotion analysis ',resized_img)

    
    #print(pre)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows

print(predicted_emotion)


# *****************************************************************
# ****************************************************************
# *************************************************************
# ***********************************************************


# ***********************PART2****************************************
# *****************************************************************
# **************************************************************


# ASKING FROM USER WHO IS YOUR FAV. ARTIST AND THEN
# FETCHING THAT PARTICULAR ARTIST TOP TRANKS AND 
# REQUIRED INFO. FROM THE SPOTIFY API


import spotipy
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


# client_id = '21f99642339d4aa5a5d9199bc60e8bf2'
# client_secret = '578a8282d52541e1acc2087e024d8698'

# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

# name = input("Whos is your favourite artist dumbo\n") #chosen artist

# result = sp.search(name) #search query
# #print(result['tracks']['items'][0]['artists'])

# #Extract Artist's uri
# artist_uri = result['tracks']['items'][0]['artists'][0]['uri']

# #Pull all of the artist's albums
# sp_albums = sp.artist_albums(artist_uri, album_type='album')

# #Store artist's albums' names' and uris in separate lists

# album_names = []
# album_uris = []

# for i in range(len(sp_albums['items'])):
#     album_names.append(sp_albums['items'][i]['name'])
#     album_uris.append(sp_albums['items'][i]['uri'])
    
# # print(album_names[5:7])
# # print(album_uris[5:7])
# #Keep names and uris in same order to keep track of duplicate albums

# #print(uri)
# def albumSongs(uri):
#     album = uri #assign album uri to a_name
#     spotify_albums[album] = {} #Creates dictionary for that specific album

#     #Create keys-values of empty lists inside nested dictionary for album
#     spotify_albums[album]['album'] = [] #create empty list
#     spotify_albums[album]['track_number'] = []
#     spotify_albums[album]['id'] = []
#     spotify_albums[album]['name'] = []
#     spotify_albums[album]['uri'] = []

#     tracks = sp.album_tracks(album) #pull data on album tracks

#     for n in range(len(tracks['items'])): #for each song track
#         spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
#         spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
#         spotify_albums[album]['id'].append(tracks['items'][n]['id'])
#         spotify_albums[album]['name'].append(tracks['items'][n]['name'])
#         spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])
        

# #albumSongs(album_uris)




# spotify_albums = {}
# album_count = 0
# for i in album_uris: #each album
#     albumSongs(i)
#     print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
#     album_count+=1 #Updates album count once all tracks have been added

# #print(spotify_albums)


# # for k, v in spotify_albums.items():
# #     names = v['name'] 
# #     #print(names)
# #     for na in names:
# #         print(na)

# # for key, values in spotify_albums:
# #     print(key + ',' + values)


# def audio_features(album):
#     #Add new key-values to store audio features
#     spotify_albums[album]['acousticness'] = []
#     spotify_albums[album]['danceability'] = []
#     spotify_albums[album]['energy'] = []
#     spotify_albums[album]['instrumentalness'] = []
#     spotify_albums[album]['liveness'] = []
#     spotify_albums[album]['loudness'] = []
#     spotify_albums[album]['speechiness'] = []
#     spotify_albums[album]['tempo'] = []
#     spotify_albums[album]['valence'] = []
#     spotify_albums[album]['popularity'] = []
#     #create a track counter
#     track_count = 0
#     for track in spotify_albums[album]['uri']:
#         #pull audio features per track
#         features = sp.audio_features(track)
        
#         #Append to relevant key-value
#         spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
#         spotify_albums[album]['danceability'].append(features[0]['danceability'])
#         spotify_albums[album]['energy'].append(features[0]['energy'])
#         spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
#         spotify_albums[album]['liveness'].append(features[0]['liveness'])
#         spotify_albums[album]['loudness'].append(features[0]['loudness'])
#         spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
#         spotify_albums[album]['tempo'].append(features[0]['tempo'])
#         spotify_albums[album]['valence'].append(features[0]['valence'])
#         #popularity is stored elsewhere
#         pop = sp.track(track)
#         spotify_albums[album]['popularity'].append(pop['popularity'])
#         track_count+=1

# import time
# import numpy as np
# sleep_min = 2
# sleep_max = 5
# start_time = time.time()
# request_count = 0
# for i in spotify_albums:
#     audio_features(i)
#     request_count+=1
#     if request_count % 5 == 0:
#         print(str(request_count) + " playlists completed")
#         time.sleep(np.random.uniform(sleep_min, sleep_max))
#         print('Loop #: {}'.format(request_count))
#         print('Elapsed Time: {} seconds'.format(time.time() - start_time))


# dic_df = {}
# dic_df['album'] = []
# dic_df['track_number'] = []
# dic_df['id'] = []
# dic_df['name'] = []
# dic_df['uri'] = []
# dic_df['acousticness'] = []
# dic_df['danceability'] = []
# dic_df['energy'] = []
# dic_df['instrumentalness'] = []
# dic_df['liveness'] = []
# dic_df['loudness'] = []
# dic_df['speechiness'] = []
# dic_df['tempo'] = []
# dic_df['valence'] = []
# dic_df['popularity'] = []
# for album in spotify_albums: 
#     for feature in spotify_albums[album]:
#         dic_df[feature].extend(spotify_albums[album][feature])
        
# len(dic_df['album'])

# import pandas as pd
# df = pd.DataFrame.from_dict(dic_df)


# print(len(df))
# final_df = df.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()
# print(len(final_df))

# print(final_df.describe())
# final_df.to_csv('artists_chartic.csv')


# ***************************************************************
# *****************################################*************
# ************######################*************************

# ***********************PART3****************************************
# *****************************************************************
# **************************************************************

##############ACCORDING TO USER'S FAV. ARTIST
#######3AND HIS MOOD RECOMMENDING HIM HIS FAVOURITE ARTIST
#########SONGS ACCORDING TO MOODS


df = pd.read_csv(r'artists_chartic.csv')


# print('************************************')
# print("1.HAPPY\n2.DISGUST\n3.SURPRISE\n4.NEUTRAL\n5.SAD\n6.ANGRY\n7.FEAR\n")
# emotions = input("Enter your emotion\n")
# print(emotions)

###emotions = ' ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

#if he is happy, make him listen sad songs
if predicted_emotion == 'happy':
    mood = float(input("On a scale from 0 to 0.1 how happy you are?\n"))
    print(mood)

#if he is supprise, make him listen slightly booooooo songs
elif predicted_emotion == 'surprise':
    mood = float(input("On a scale from 0.1 to 0.25 how surprise you are?\n"))
    print(mood) 

#if he is neutral, make him listen slightly better songs
elif predicted_emotion == 'neutral':
    mood = float(input("On a scale from 0.25 to 0.50 how neutral you are?\n"))
    print(mood)

#if he is disgust, make him listen good songs
elif predicted_emotion == 'disgust':
    mood = float(input("On a scale from 0.50 to 0.75 how disgust you are?\n"))
    print(mood)

#if he is scared, make him listen better songs
elif predicted_emotion == 'fear':
    mood = float(input("On a scale from 0.75 to 0.90 how scared you are?\n"))
    print(mood)

#if he is sad or angry, make him listen happy songs
else:
    mood = float(input("On a scale from 0.90 to 1 how sad or angry you are?\n"))
    print(mood)

print('************************************')

#songs = pd.DataFrame()

links = []
names = []

if mood < 0.10:
    for i in range(len(df)):
        if any ( [ (0 <= df.loc[i,"valence"] <= (mood + 0.15)),(df.loc[i,"danceability"] <= (mood*8)) , (df.loc[i,"energy"] <= (mood*10))]):
            links.append(df.loc[i,"uri"])
            names.append(df.loc[i,'name'])
            
elif 0.10 <= mood < 0.25:
    for i in range(len(df)):
        if all ([(mood - 0.075) <= df.loc[i,"valence"] <= (mood + 0.075),df.loc[i,"danceability"] <= (mood*4),df.loc[i,"energy"] <= (mood*5)]):
            links.append(df.loc[i,"uri"])
            names.append(df.loc[i,'name'])

elif 0.25 <= mood < 0.50:
    for i in range(len(df)):
        if all ([(mood - 0.05) <= df.loc[i,"valence"] <= (mood + 0.05),df.loc[i,"danceability"] <= (mood*1.75),df.loc[i,"energy"] <= (mood*1.75)]):
                links.append(df.loc[i,"uri"])
                names.append(df.loc[i,'name'])

elif 0.50 <= mood < 0.75:
    for i in range(len(df)):                        
        if all ([(mood - 0.075) <= df.loc[i,"valence"] <= (mood + 0.075),df.loc[i,"danceability"] >= (mood/2.5),df.loc[i,"energy"] >= (mood/2)]):
            links.append(df.loc[i,"uri"])
            names.append(df.loc[i,'name'])

elif 0.75 <= mood < 0.90:    
    for i in range(len(df)):                    
        if all ([(mood - 0.075) <= df.loc[i,"valence"] <= (mood + 0.075),df.loc[i,"danceability"] >= (mood/2),df.loc[i,"energy"] >= (mood/1.75)]):
            links.append(df.loc[i,"uri"])
            names.append(df.loc[i,'name'])

elif mood >= 0.90:
    for i in range(len(df)):
        if all ([(mood - 0.15) <= df.loc[i,"valence"] <= 1,df.loc[i,"danceability"] >= (mood/1.75),df.loc[i,"energy"] >= (mood/1.5)]):
            links.append(df.loc[i,"uri"])
            names.append(df.loc[i,'name'])
            
else:
    print("Try another mood")

#print(links + names)

# print(links)
# print(names)

# for j in range(len(links)):
#     print(str(j) +'. LINKS : '+ links[j] + '  |  NAMES : ' + names[j])
#     # bf = pd.DataFrame(links[j], columns='URI')
#     # bf.head()

# *************************************************************
# ********************************************************
# *************************************************
# *******************************************

# ***********************PART4****************************************
# *****************************************************************
# **************************************************************


# ************************************Python3 code for movie 
# ***********************************recommendation based on 
#****************************************** emotion 
  
# Import library for web 
# scrapping 
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 
  
# Main Function for scraping 
def main(emotion): 

    # IMDb Url for Drama genre of 
    # movie against emotion Sad 
    if(emotion == "Sad" or emotion == "sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Musical genre of 
    # movie against emotion Disgust 
    elif(emotion == "Disgust" or emotion == "disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Family genre of 
    # movie against emotion Anger 
    elif(emotion == "Anger" or emotion == "anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Thriller genre of 
    # movie against emotion Anticipation 
    elif(emotion == "neutral" or emotion == "neutral"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
  # IMDb Url for Sport genre of 
    # movie against emotion Fear 
    elif(emotion == "Fear" or emotion == "fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Thriller genre of 
    # movie against emotion Enjoyment 
    elif(emotion == "Happy" or emotion == "happy"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Western genre of 
    # # movie against emotion Trust 
    # elif(emotion == "Trust" or emotion == "trust"): 
    #     urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Film_noir genre of 
    # movie against emotion Surprise 
    elif(emotion == "Surprise" or emotion == "surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    # HTTP request to get the data of 
    # the whole page 
    response = HTTP.get(urlhere) 
    data = response.text 
  
    # Parsing the data using 
    # BeautifulSoup 
    soup = SOUP(data, "lxml") 
  
    # Extract movie titles from the 
    # data using regex 
    b = soup.find_all('h3',{'class':'lister-item-header'})
    #c = b.findAll()

    return b
    # title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    # return title 

    # Driver Function 
if __name__ == '__main__': 
    

    # print("What is your mood right now shitbag:\n")
    # print('************************************')
    # print("1.Sad\n2.Disgust\n3.Anger\n4.Neutral\n5.Fear\n6.Happy\n7.Surprise")
    #NEUTRAL
    
    #emotion = input("Enter the emotion: ")
    
    print('************************************')
    
    a = main(predicted_emotion)
    
    movi = []
    
    for c in a:
        #print("Movies : " + c.find_all('a')[0].text)
        movi.append(c.find_all('a')[0].text)

    #print(movi)


# *****************************************************************************
# *********************************************************************
# *********************************************************
# *************************************************

# print(links)
# print(names)
# print(movi)

import sqlite3 
  
conn = sqlite3.connect('pythonDB.db') 
c = conn.cursor() 
  
def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (SONGS_NAMES TEXT, URI TEXT, MOVIE_NAMES TEXT)') 
  
def data_entry(): 
    c.execute("INSERT INTO RecordONE (SONGS_NAMES, URI, MOVIE_NAMES) VALUES(?, ?, ?)" , (names, links, movi)) 
    conn.commit() 
  
create_table() 
data_entry() 
  
c.close() 
conn.close() 
import pandas as pd

import numpy as numpy

df = pd.read_csv(r'artists_chartic.csv')

# print(df.head())
# print(df.describe())

# energy = df['energy']
# valence = df['valence']
# dance = df["danceability"]

#print(energy)
print("What is your mood right now shitbag:\n")
print('************************************')
#print("1.Sad\n2.Disgust\n3.Anger\n4.Anticipation\n5.Fear\n6.Enjoyment\n7.Trust\n8.Surprise")
    
mood = float(input("Enter the emotion: "))
    
print('************************************')

#songs = pd.DataFrame()
sel = []

if mood < 0.10:
    if (0 <= df["valence"] <= (mood + 0.15)
        & df["danceability"] <= (mood*8)
        & df["energy"] <= (mood*10)):
        sel.append(df["uri"])
 
else:
    print("FUCK OFF")

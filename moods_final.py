import pandas as pd

df = pd.read_csv(r'artists_chartic.csv')

# print(df.head())
# print(df.describe())

# energy = df['energy']
# valence = df['valence']
# dance = df["danceability"]

#print(energy)
print("What is your mood right now :\n")
#print('************************************')
#print("1.Sad\n2.Disgust\n3.Anger\n4.Anticipation\n5.Fear\n6.Enjoyment\n7.Trust\n8.Surprise")
    
mood = float(input("Enter the emotion: "))
    
print('************************************')

#songs = pd.DataFrame()
sel = []
if mood < 0.10:
    for i in range(len(df)):
        if any ( [ (0 <= df.loc[i,"valence"] <= (mood + 0.15)),(df.loc[i,"danceability"] <= (mood*8)) , (df.loc[i,"energy"] <= (mood*10))]):
            sel.append(df.loc[i,"uri"])
            sel.append(df.loc[i,'name'])
            
elif 0.10 <= mood < 0.25:
    for i in range(len(df)):
        if all ([(mood - 0.075) <= df.loc[i,"valence"] <= (mood + 0.075),df.loc[i,"danceability"] <= (mood*4),df.loc[i,"energy"] <= (mood*5)]):
            sel.append(df.loc[i,"uri"])
            sel.append(df.loc[i,'name'])

elif 0.25 <= mood < 0.50:
    for i in range(len(df)):
        if all ([(mood - 0.05) <= df.loc[i,"valence"] <= (mood + 0.05),df.loc[i,"danceability"] <= (mood*1.75),df.loc[i,"energy"] <= (mood*1.75)]):
                sel.append(df.loc[i,"uri"])
                sel.append(df.loc[i,'name'])

elif 0.50 <= mood < 0.75:
    for i in range(len(df)):                        
        if all ([(mood - 0.075) <= df.loc[i,"valence"] <= (mood + 0.075),df.loc[i,"danceability"] >= (mood/2.5),df.loc[i,"energy"] >= (mood/2)]):
            sel.append(df.loc[i,"uri"])
            sel.append(df.loc[i,'name'])

elif 0.75 <= mood < 0.90:    
    for i in range(len(df)):                    
        if all ([(mood - 0.075) <= df.loc[i,"valence"] <= (mood + 0.075),df.loc[i,"danceability"] >= (mood/2),df.loc[i,"energy"] >= (mood/1.75)]):
            sel.append(df.loc[i,"uri"])
            sel.append(df.loc[i,'name'])

elif mood >= 0.90:
    for i in range(len(df)):
        if all ([(mood - 0.15) <= df.loc[i,"valence"] <= 1,df.loc[i,"danceability"] >= (mood/1.75),df.loc[i,"energy"] >= (mood/1.5)]):
            sel.append(df.loc[i,"uri"])
            sel.append(df.loc[i,'name'])
            
else:
    print("Try another mood")

print(sel)
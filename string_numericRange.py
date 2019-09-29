import pandas as pd

df = pd.read_csv(r'artists_chartic.csv')

emotions = input("Enter your emotion\n")
print(emotions)

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

# def sad():
#     i = ' for i in range(0.1)
#     print( i

#emotions = ' ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

#if he is happy, make him listen sad songs
if emotions == 'happy':
    num = float(input("On a scale from 0 to 0.1 how disgust you are?\n"))
    print(num)

#if he is supprise, make him listen slightly booooooo songs
elif emotions == 'surprise':
    num = float(input("On a scale from 0.1 to 0.25 how angry you are?\n"))
    print(num) 

#if he is neutral, make him listen slightly better songs
elif emotions == 'neutral':
    num = float(input("On a scale from 0.25 to 0.50 how scared you are?\n"))
    print(num)

#if he is disgust, make him listen good songs
elif emotions == 'disgust':
    num = float(input("On a scale from 0.50 to 0.75 how disgust you are?\n"))
    print(num)

#if he is scared, make him listen better songs
elif emotions == 'sad':
    num = float(input("On a scale from 0.75 to 0.90 how sad you are?\n"))
    print(num)

#if he is sad or angry, make him listen happy songs
else:
    num = float(input("On a scale from 0.90 to 1 how sad or angry you are?\n"))
    print(num)


emotions = input("Enter your emotion\n")
print(emotions)

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


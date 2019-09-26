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
        #if he is happy, make him listen sad songs
        if predicted_emotion == 'happy':
            num = float(input("On a scale from 0 to 0.1 how disgust you are?\n"))
            print(num)
            break

        #if he is supprise, make him listen slightly booooooo songs
        elif predicted_emotion == 'surprise':
            num = float(input("On a scale from 0.1 to 0.25 how angry you are?\n"))
            print(num)
            break

        #if he is neutral, make him listen slightly better songs
        elif predicted_emotion == 'neutral':
            num = float(input("On a scale from 0.25 to 0.50 how scared you are?\n"))
            print(num)
            break

        #if he is disgust, make him listen good songs
        elif predicted_emotion == 'disgust':
            num = float(input("On a scale from 0.50 to 0.75 how disgust you are?\n"))
            print(num)
            break

        #if he is scared, make him listen better songs
        elif predicted_emotion == 'sad':
            num = float(input("On a scale from 0.75 to 0.90 how sad you are?\n"))
            print(num)
            break

        #if he is sad or angry, make him listen happy songs
        else:
            num = float(input("On a scale from 0.90 to 1 how sad or angry you are?\n"))
            print(num)
            break


        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial emotion analysis ',resized_img)

    
    #print(pre)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows

print(predicted_emotionpre)
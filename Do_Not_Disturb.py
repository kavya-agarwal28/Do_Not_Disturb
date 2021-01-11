import numpy as np
import cv2
import pyautogui

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
count = 1

while(True):
    ret,img = cap.read()
    cv2.resizeWindow('img',500,500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        xx = int(x+(x+w))/2
        yy = int(y+(y+h))/2
        print(xx)
        print(yy)
        center = (xx,yy)
        print("Center of Rectangle is :", center)
        
    cv2.imshow('img',img)
    
    if xx>=300 and xx<=350 and yy>=230 and yy<=250 and count==1:
        pyautogui.press('space')
        count=0
        print("AAAAA")

    elif xx>=230 and xx<=300 and yy>=250 and yy<=290 and count==0:
        pyautogui.press('space')
        count=1
        print("BBBBB")
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
        
cap.release()
cv2.destroyAllWindows()
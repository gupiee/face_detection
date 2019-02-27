import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("E:/Users/admin/AppData/Local/Programs/Python/Python35/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

img=cv2.imread("C:/Users/admin/Pictures/Screenshots/ty.jpg")

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0.255,0),3)

cv2.imshow("tony stark",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
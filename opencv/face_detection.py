import cv2
import os
import time
import sys

face_cascade = cv2.CascadeClassifier("C:\\Users\\kanok\\Documents\\lbpcascade_animeface.xml")
cv2.ocl.setUseOpenCL(1)
cap = cv2.VideoCapture("D:\\backup-usb\\test_vid\\gochuumon2_9.mp4")
num = 0
while 1:
    ret, img1 = cap.read()
    img = cv2.resize(img1, (0, 0), fx=1, fy=1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (175, 244, 65), 1)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]

        #cv2.imwrite('C:\\Users\\kanok\\Documents\\python-sktch\\opencv\\image_save\\image_'+str(num)+'.jpg', roi_color) #save img to folder
        cv2.imshow("face-output", roi_color)
        num += 1
    cv2.imshow("gochiusa_opencv", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    cap.release()
    cv2.destroyAllWindows()


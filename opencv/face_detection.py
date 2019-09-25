import cv2
import os
import time
import sys

face_cascade = cv2.CascadeClassifier("path to .xml files")
cv2.ocl.setUseOpenCL(1)
cap = cv2.VideoCapture(0)
num = 0

while True:
    ret, img1 = cap.read()
    img = cv2.resize(img1, (0, 0), fx=1, fy=1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (175, 244, 65), 1)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
        cv2.imshow("face-output", roi_color)
        num += 1
    cv2.imshow("output", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    cap.release()
    cv2.destroyAllWindows()

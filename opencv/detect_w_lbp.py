import os
import time
import cv2

def detect_w_lbp():
    cv2.ocl.setUseOpenCL(1)
    haar = cv2.CascadeClassifier("C:\\Users\\kanok\\Documents\\lbpcascade_animeface.xml")
    cap = cv2.VideoCapture("D:\\backup-usb\\test_vid\\gochuumon2_9.mp4")
    reg = cv2.face.LBPHFaceRecognizer_create() 
    reg.read("C:\\Users\\kanok\\Documents\\python-sktch\\opencv\\lbp_folder\\out.yml")
       
    while True:
        face_id = 0
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = haar.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x+w, y+h), (175, 244, 65), 1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            face_id, conf = reg.predict(roi_gray)
            if face_id == 1:
                cv2.rectangle(img, (x, y), (x+w, y+h), (244, 196, 65), 3)
                #cv2.imshow("Chino", roi_color)
                face_name = "Chino"
                cv2.putText(img,str(face_name), (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (244, 196, 65))
            elif face_id == 2:
                cv2.rectangle(img, (x, y), (x+w, y+h), (65, 128, 244), 3)
                #cv2.imshow("Cocoa", roi_color)
                face_name = "Cocoa"
                cv2.putText(img,str(face_name), (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (65, 128, 244))
            elif face_id == 3:
                cv2.rectangle(img, (x, y), (x+w, y+h), (244, 65, 143), 3)
                #cv2.imshow("Rize", roi_color)
                face_name = "Rize"
                cv2.putText(img,str(face_name), (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (244, 65, 143))
            elif face_id == 4:
                cv2.rectangle(img, (x, y), (x+w, y+h), (65, 238, 244), 3)
                #cv2.imshow("Syaro", roi_color)
                face_name = "Syaro"
                cv2.putText(img,str(face_name), (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (65, 238, 244))
            elif face_id == 5:
                cv2.rectangle(img, (x, y), (x+w, y+h), (65, 244, 71), 3)
                #cv2.imshow("Chiya", roi_color)
                face_name = "Chiya"
                cv2.putText(img,str(face_name), (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (65, 244, 71))
        cv2.imshow("detection with LBP", img)
        k = cv2.waitKey(1) and 0xff
        if k == 27:
            break

if __name__ == "__main__":
    detect_w_lbp()


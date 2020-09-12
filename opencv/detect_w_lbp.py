import cv2

#haar = cv2.CascadeClassifier("path to .xml")
#reg.read("path to .yml")
haar = cv2.CascadeClassifier("./animeface.xml")
cap = cv2.VideoCapture("./test.mp4")
reg = cv2.face.LBPHFaceRecognizer_create() 
reg.read("./gochi.yml")

face_name = {'Chino':(244, 196, 65), 
              'Cocoa':(65, 128, 244), 
              'Rize':(244, 65, 143),
              'Sharo':(65, 238, 244),
              'Chiya':(65, 244, 71)
}

def detect_w_lbp():
  while cap.isOpened():
    ret, img = cap.read()
    if not ret:
      break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray, 1.3, 3)
    for(x, y, w, h) in faces:
      roi_gray = gray[y:y+h, x:x+w]
      face_id, conf = reg.predict(roi_gray)
      for idx, (name, colo_val) in enumerate(face_name.items()):
        if idx == face_id and conf > 70:
          cv2.rectangle(img, (x, y), (x+w, y+h), colo_val, 1)
          cv2.putText(img, f'{name}, {conf:.2}', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, colo_val)
    cv2.imshow("detection with LBP", img)
    if cv2.waitKey(1) == ord('q'):
      break
  cap.release()
  cv2.destroyAllWindows()
  exit()

if __name__ == "__main__":
  detect_w_lbp()

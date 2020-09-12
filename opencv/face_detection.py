import cv2

face_cascade = cv2.CascadeClassifier("./animeface.xml")
cap = cv2.VideoCapture('./test.mp4')
num = 0

while cap.isOpened():
    ret, img = cap.read()
    if ret is None:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (175, 244, 65), 1)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
        cv2.imshow("output", img)
        cv2.imwrite(f'./img_save/img_{num}.jpg', roi_color)
    num += 1
    if cv2.waitKey == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

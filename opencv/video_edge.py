import cv2

cv2.ocl.setUseOpenCL(1)
cap = cv2.VideoCapture('./gochuumon2_9.mp4') # change video path

while 1:
  _, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  edge = cv2.Canny(gray, 75, 125)
  cv2.imshow('edge', edge)
  if cv2.waitKey(1) == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

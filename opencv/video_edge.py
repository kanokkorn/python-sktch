import cv2

cv2.ocl.setUseOpenCL(1)
cap = cv2.VideoCapture('./gochuumon2_9.mp4') # change video path

while 1:
  _, img = cap.read()
  if _ is 'false' print('Video not available')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

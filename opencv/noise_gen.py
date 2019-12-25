import cv2
import numpy as np

img = cv2.imread('../img/shyaro.jpg') 

gray = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for i in img]
gray = [np.float64(i) for i in gray]
noise = np.random.randn(*gray[1].shape)*100
noisy = [i+noise for i in gray]
noisy = [np.uint8(np.clip(i, 0, 255)) for i in noisy]

cv2.imshow('noise', noisy[2])
cv2.waitKey()

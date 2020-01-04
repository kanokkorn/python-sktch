import cv2
import numpy as np
img = cv2.imread('../img/shyaro.jpg')
mask = np.zeros(img.shape[:2] ,np.uint8)

src = np.zeros((1, 65), np.float64)
sub = np.zeros((1, 65), np.float64)
rect = (161, 79, 150, 150)

cv2.grabCut(img, mask, rect, src, sub, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

img = img*mask2[:,:,np.newaxis]

cv2.imshow('cut', img)
cv2.waitKey()
cv2.DestroyAllWindow()

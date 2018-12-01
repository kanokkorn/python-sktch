import cv2 
import numpy as np
from matplotlib import pyplot as plt

imgL = cv2.imread('C:\\Users\\kanok\\Downloads\\24760885.jpg',0)
imgR = cv2.imread('C:\\Users\\kanok\\Downloads\\24760885.jpg',0)

#stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,ndisparities=16, SADWindowSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode, ZBarSymbol
import cv2
import numpy as np 

image = cv2.imread('C:\\Users\\GEFORCE\\Documents\\img-qr2.png') 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# calculate points for each contour
hull = []
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))

drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
 
# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    #cv2.drawContours(drawing, hull, i, color, 1, 8)

cv2.imshow("Thresh", drawing)
cv2.waitKey()
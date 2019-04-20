import cv2
import numpy as np
from pyzbar.pyzbar import decode
from matplotlib import pyplot as plt 

print(cv2.__version__)
img = cv2.imread('C:\\Users\\GEFORCE\\Documents\\img-qr1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img, cmap = 'gray')
plt.figure(figsize = (9, 5))
plt.imshow(img, cmap = 'gray')  
plt.title('Original QR images')

for code in decode(img):
    points = code.polygon
    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
        hull = list(map(tuple, np.squeeze(hull)))
    else : 
        hull = points
    # Number of points in the convex hull
    n = len(hull)     
    
    for j in range(0,n):
        cv2.line(img, hull[j], hull[ (j+1) % n], (255,0,0), 3)
    
    # draw text    
    x = code.rect.left
    y = code.rect.top    
    w = code.rect.width 
    h = code.rect.height
    
    # draw bounding box
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    barCode = str(code.data)
    cv2.putText(img, barCode, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
    
# Draw output
plt.figure(figsize = (9, 5))
plt.imshow(img, cmap = 'gray') 
plt.title('Labeled QR images')
cv2.imshow('QR_Image/QR_complex_labeld.png', img)
cv2.waitKey()
import cv2
import numpy

# TODO: change VideoCapture() to camera ID

capture = cv2.VideoCapture(0)

width = capture.get(cv2.CAP_PROP_FRAME_WIDTH )
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT )

print("Resolution is {:.0f} x {:.0f} ".format(width ,height))

#This loop run forever
while True:
    
    ret, img = capture.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # TODO: Draw reference line for angle calculation
    
    cv2.lineline(imgray, pt1, pt2, color[, thickness[, lineType[, shift]]])
    cv2.imshow("Observer", imgray)
    
    # Press 'Q' to exit program
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
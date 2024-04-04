import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow('RGB track bar')
cv2.createTrackbar('red color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('green color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('blue color', 'RGB track bar', 0, 255, nothing)

cv2.setTrackbarPos('red color', 'RGB track bar', 125)
cv2.setTrackbarPos('green color', 'RGB track bar', 125)
cv2.setTrackbarPos('blue color', 'RGB track bar', 125)

img = np.zeros((512,512,3) ,np.uint8)

while(1):
    redVal = cv2.getTrackbarPos('red color', 'RGB track bar')
    greenVal = cv2.getTrackbarPos('green color', 'RGB track bar')
    blueVal = cv2.getTrackbarPos('blue color', 'RGB track bar')

    print(redVal)

    cv2.rectangle(img, (0,0), (512,512), (blueVal, greenVal, redVal), -1)
    cv2.imshow('RGB track bar', img)

    if cv2.waitKey(30) & 0xFF == 27:
        break
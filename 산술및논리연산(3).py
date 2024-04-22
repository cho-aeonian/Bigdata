import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('./../images/img1.jpg')
img2 = cv2.imread('./../images/img2.jpg')
img3 = cv2.imread('./../images/img3.jpg')
img4 = cv2.imread('./../images/img4.jpg')
img5 = cv2.imread('./../images/img5.jpg')

print(img5.shape)

# 마스크 선언 및 초기화
mask = np.full(shape=img5.shape, fill_value=0, dtype=np.uint8)
h, w, c = img5.shape
x = (int)(w/2) - 60; y = (int)(h/2) - 60
cv2.rectangle(mask, (x,y), (x+120, y+120), (255,255,255), -1)

# 산술 및 논리 연산 수행
ress = []
ress.append(cv2.add(img1, img2))
ress.append(cv2.addWeighted(img1, 0.5,img2, 0.5, 0))
ress.append(cv2.subtract(img3, img4))
ress.append(cv2.absdiff(img3, img4))
ress.append(cv2.bitwise_not(img5))
ress.append(cv2.bitwise_not(img5, mask))
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("C:\Bigdata(class)\corner\img_6_4.png",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src, (320,240))

dst = cv2.cornerHarris(img1,2,3,0.06)
dst = cv2.dilate(dst,None)
res1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
res1[dst>0.1*dst.max()] = [0,0,255]

displays = [("input1",img1),("res1",res1)]
for (name, out) in displays:
    cv2.imshow(name, out)

cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src= cv2.imread("C:\Bigdata(class)\hough transform\img_6_0.png", cv2.IMREAD_GRAYSCALE)
img2_src = cv2.imread("C:\Bigdata(class)\hough transform\img_6_3.png",cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1_src,(320,240))
img2 = cv2.resize(img2_src, (320,240))

img1_edge = cv2.Canny(img1, 50, 150, apertureSize=3)
lines = cv2.HoughLines(img1_edge, 2, np.pi/180,100)
linesP = cv2.HoughLines(img1_edge, 2, np.pi/180, 50, minLineLength=1, maxLineGap=100)
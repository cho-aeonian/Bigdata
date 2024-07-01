import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("C:\Bigdata(class)\corner\img_6_4.png",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src, (320,240))
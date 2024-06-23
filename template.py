import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("C:\Bigdata(class)\templete\img_6_0.png",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src,(320,240))
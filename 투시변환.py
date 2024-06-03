import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("C:\Bigdata(class)\Perspective Transform\img12.jpg",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1,(320,240))
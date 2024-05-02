import cv2
import numpy as np
from matplotlib import pyplot as plt

# 영상 읽기
img1 = cv2.imread("C:\img6\img6.jpg", cv2.IMREAD_GRAYSCALE)

# 히스토그램 평활화 및 히스토그램 계산
res1 = cv2.equalizeHist(img1)
ch1 = [0]; ranges1 = [0,256]; histSize1 = [256]
hist1 = cv2.calcHist([img1], ch1, None, histSize1, ranges1)
hist2 = cv2.calcHist([res1], ch1, None, histSize1, ranges1)
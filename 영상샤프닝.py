import numpy as np
import cv2
from matplotlib import pyplot as plt

# 영상 밝기
img1 = cv2.imread("C:\Bigdata(class)\img8\img8.jpg", cv2.IMREAD_GRAYSCALE)

# 샤프닝 수행
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
res1 = cv2.filter2D(img1, -1, kernel)
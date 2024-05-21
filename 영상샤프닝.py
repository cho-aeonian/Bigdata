import numpy as np
import cv2
from matplotlib import pyplot as plt

# 영상 밝기
img1 = cv2.imread("C:\Bigdata(class)\img8\img8.jpg", cv2.IMREAD_GRAYSCALE)

# 샤프닝 수행
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
res1 = cv2.filter2D(img1, -1, kernel)

# 언샤프 기법 수행
ksize1 = 3; ksize2 = 15
img1_blur1 = cv2.blur(img1, (ksize1, ksize1))
img1_blur2 = cv2.blur(img1, (ksize2, ksize2))
res2 = cv2.subtract(img1.astype(np.uint16)*1, img1_blur1.astype(np.uint16))
res3 = cv2.subtract(img1.astype(np.uint16)*1, img1_blur1.astype(np.uint16))
res2 = cv2.astype(np.uint8); res3 = res3.astype(np.uint8)

dif_img1 = cv2.absdiff(img1, img1_blur1)
dif_img2 = cv2.absdiff(img1, img1_blur2)
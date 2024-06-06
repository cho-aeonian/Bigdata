import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("C:\Bigdata(class)\Perspective Transform\img12.jpg",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1,(320,240))

h, w = img1.shape
point1_src = np.float32([[1,1],[2-10,10],[5,h-5],[2-4,h-4]])
point1_dst = np.float32([[15,15],[2-60,15],[10,h-25],[2-100,h-50]])
point2_src = np.float32([[148,145],[168,144],[136,223],[188,222]])
point2_dst = np.float32([[136,145],[168,144],[136,223],[188,222]])
per_mat1 = cv2.getPerspectiveTransform(point1_src,point1_dst)
per_mat2 = cv2.getPerspectiveTransform(point2_src,point2_dst)
res1 = cv2.warpPerspective(img1, per_mat1, (w,h))
res2 = cv2.warpPerspective(img1, per_mat2, (w,h))

ress = [];
ress.append(img1),ress.append(res1), ress.append(res2)
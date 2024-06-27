import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("C:\Bigdata(class)\templete\img_6_0.png",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src,(320,240))

template = img1[5:70,5:70]
w, h = template.shape[::-1]
methods = ['cv2.TM_CCOEFF','cv2.TM_CCIEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for meth in methods:
    input = img1.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img1,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
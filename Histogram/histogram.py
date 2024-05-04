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

# 상수곱, 로그곱, 거듭제곱 반환 기반 명암비 조절 및 히스토그램 계산
multi_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
log_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
invol1_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
multi_v = 2; gamma1 = 0.4
thres1 = 5; thres2 = 100
max_v_log = 255 / np.log(1+255)
max_v_invol1 = 255 / np.power(255, gamma1)

for i in range(256):
    val = i * multi_v
    if val > 255 : val = 255
    multi_lut[i] = val
    log_lut[i] = np.round(max_v_log * np.log(1+i))
    invol1_lut[i] = np.round(max_v_invol1 * np.power(i, gamma1))
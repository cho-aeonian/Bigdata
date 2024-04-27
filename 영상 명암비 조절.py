import cv2
import numpy as np
from matplotlib import pyplot as plt

# 영상 읽기
img1 = cv2.imread("./../images/img5.jpg",cv2.IMREAD_GRAYSCALE)

if img1 is None:
    print('no file found')
    exit()

# 영상 명암비 조절 변수 선언 및 초기화
multi_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
log_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
invol_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
sel_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)

multi_v = 2; gamma1 = 0.1; gamma2 = 0.6
thres1 = 5; thres2 = 100

max_v_log = 255 / np.log(1+255)
max_v_invol = 255 / np.power(255,gamma1)
max_v_sel = 100 / np.power(thres2, gamma2)
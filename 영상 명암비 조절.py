import cv2
import numpy as np
from matplotlib import pyplot as plt

# 영상 읽기
img1 = cv2.imread("./../images/img5.jpg",cv2.IMREAD_GRAYSCALE)

if img1 is None:
    print('no file found')
    exit()
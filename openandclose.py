import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("C:\Bigdata(class)\openclose\img13.jpg",cv2.IMREAD_GRAYSCALE)

methods = [cv2.MORPH_OPEN,
           cv2.MORPH_CLOSE,
           cv2.MORPH_GRADIENT,
           cv2.MORPH_TOPHAT,
           cv2.MORPH_BLACKHAT,
           cv2.MORPH_HITMISS]
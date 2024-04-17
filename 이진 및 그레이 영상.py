import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 그림 파일 불러오기
img =  cv.imread('puppy.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# 이진화 수행하기
ret, thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# 그림별 제목 정하기
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

# 동시에 여러 그림 출력하기
images = [img, thresh1 ,thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title
    plt.xticks([]),plt.yticks([])
plt.show()
import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('./../images/img5.jpg', 0)

# 영상 밝기 조절 변수 선언 및 초기화
v = np.full(shape=img1.shape, fill_value=100, dtype=np.uint8)
v_n = np.full(shpe=img1.shpe, fill_value=255, dtype=np.uint8)

# 영상 밝기 조절
# res1은 파이썬 결과, res2과 res3는 OpenCV에서 제공하는 함수를 사용한 결과
ress = []
ress.append(img1)
ress.append(np.uint8(img1+v))
ress.append(cv2.add(img1, v))
ress.append(cv2.subtract(v_n, img1))

titles = ['input','add','add2','sub']
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
import os
import cv2

cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image',frame)

        key = cv2.waitKey(30) & 0xFF

        #시간을 늦추면 어떻게 될까요?
        # key = cv2.waitKey(100) & 0xFF
        if(key==27):
            break
        else:
            break

# 다 썼으면 release 해주세요 !!!
cap.release()

# 창 닫고 끝냅시다.
cv2.destoryAllWindows()
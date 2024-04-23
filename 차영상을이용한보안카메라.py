import cv2
import numpy as np

CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID)
if not cam.isOpened():
    print('Cannot open the camera-%d' % (CAMERA_ID))
    exit()

cv2.namedWindow('CAM Window')

# 배경 영상 초기화
background = None

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 회색 영상으로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('CAM Window', gray_frame)

    key = cv2.waitKey(33)

    # 'a' 키를 누르면 배경 영상 촬영
    if key == ord('a'):
        background = gray_frame.copy()
        print("Background captured.")

    # 'b' 키를 누르면 차영상을 이진화
    elif key == ord('b'):
        if background is not None:
            # 차영상 계산
            diff = cv2.absdiff(background, gray_frame)

            # 차영상을 이진화
            _, binary_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

            # 이진화된 차영상을 표시
            cv2.imshow('Binary Difference', binary_diff)

    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        break

# 종료 시 카메라 리소스 해제
cam.release()
cv2.destroyAllWindows()

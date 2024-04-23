import cv2

# 웹캠 설정
CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID)
if not cam.isOpened():
    exit('Cannot open the camera')

# 창 생성
cv2.namedWindow('CAM Window')

# 배경 영상 초기화
background = None

while True:
    # 영상 프레임 읽기
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 회색조 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('CAM Window', gray_frame)

    # 배경 영상이 촬영되었다면
    if background is not None:
        # 차영상 계산
        diff_frame = cv2.absdiff(gray_frame, background)
        idsplay_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] if apply_threshold else diff_frame
    else:
        display_frame = gray_frame

    # 이진화된 차영상 표시
    cv2.imshow('Binary Difference', diff_frame)

    # 움직임 감지를 위해 이진화된 차영상에서 윤곽선 검출
    contours, _ = cv2.findContours(diff_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #키보드
    key = cv2.waitKey(33)  
    # 'q' 키를 누르면 종료
    if key == ord('q'):
        break
    # 'a' 키를 누르면 배경 영상 촬영
    if key == ord('a'):
        background = gray_frame.copy()
    # 'b' 키를 누르면 배경 이진화
    if key == ord('b'):
        apply_threshold = not apply_threshold

# 종료 시 카메라 리소스 해제
cam.release()
cv2.destroyAllWindows()

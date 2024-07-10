import numpy as np
import cv2
from matplotlib import pyplot as plt

def nothing(x):
    pass

def check_odd(num):
    if num % 2 == 0:
        num += 1
    return num

def set_run(pos):
    global img1
    method = cv2.getTrackbarPos('method',"morphology")
    itr = cv2.getTrackbarPos('iter',"morphology")
    ksize = cv2.getTrackbarPos('ksize', "morphology")
    run = cv2.getTrackbarPos('run',"morphology")
    if run == 1:
        ksize = check_odd(ksize)
        kernel = cv2.getStructuringElement(cv2.MORPH_RE, (ksize, ksize))
        if method == 0:
            res = cv2.erode(img1, kernel, iterations=itr)
        else:
            res = cv2.dilate(img1, kernel, iterations=itr)
        cv2.imshow("morphology",res)
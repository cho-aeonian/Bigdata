import numpy as np
import cv2
from matplotlib import pyplot as plt

def nothing(x):
    pass

def check_odd(num):
    if num % 2 == 0:
        num += 1
    return num
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the image in grayscale and resize it
img1 = cv2.imread("C:/Bigdata(class)/geometry conversion/mouse.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (320, 240))

# Create a copy of the image to draw points on
img_with_points = img1.copy()
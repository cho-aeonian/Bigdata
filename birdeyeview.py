import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the image in grayscale and resize it
img1 = cv2.imread("C:/Bigdata(class)/geometry conversion/mouse.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (320, 240))

# Create a copy of the image to draw points on
img_with_points = img1.copy()

# Initialize an empty list to store the points
points = []

def draw_rect(event, x, y, flags, param):
    global points, img_with_points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))
            # Draw a small circle to indicate the points clicked
            cv2.circle(img_with_points, (x, y), 5, (255, 0, 0), -1)
            cv2.imshow('image', img_with_points)

# Create a window and set a mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)

# Ensure we have 4 points
if len(points) == 4:
    # Define the points in the destination image
    width, height = 320, 240
    dst_points = np.array([
        [0, height], 
        [0, 0], 
        [width, 0], 
        [width, height]
    ], dtype="float32")

    # Convert the points to numpy array
    src_points = np.array(points, dtype="float32")
    
    # Compute the perspective transform matrix
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply the perspective transformation to the image
    warped = cv2.warpPerspective(img1, M, (width, height))

     # Display the original image with points and the transformed image
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(cv2.cvtColor(img_with_points, cv2.COLOR_BGR2RGB), cmap='gray'), plt.title('Input with Points')
    plt.subplot(122), plt.imshow(warped, cmap='gray'), plt.title('Bird\'s Eye View')
    plt.show()
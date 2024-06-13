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

# Display the image and wait for 4 points to be clicked
while True:
    cv2.imshow('image', img_with_points)
    if len(points) == 4:
        break
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'ESC' to exit
        break

cv2.destroyAllWindows()

# Ensure we have 4 points
if len(points) == 4:
    # Convert the points to numpy array
    src_points = np.array(points, dtype="float32")

    # Find the bounding box for the clicked points
    rect = cv2.boundingRect(src_points)
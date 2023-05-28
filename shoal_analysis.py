import cv2
import numpy as np
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to get binary image
_, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# Find contours of black dots
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Identify the XY pixel positions of the dots
dot_positions = []
for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        dot_positions.append((x, y))

# Calculate distances between each pair of points
num_dots = len(dot_positions)
distances = np.zeros((num_dots, num_dots))
for i in range(num_dots):
    for j in range(i + 1, num_dots):
        distance = calculate_distance(dot_positions[i], dot_positions[j])
        distances[i, j] = distance
        distances[j, i] = distance

# Calculate the average pairwise distance
total_distance = np.sum(distances)
average_distance = total_distance / (num_dots * (num_dots - 1) / 2)

# Print the average pairwise distance
print("Average Pairwise Distance:", average_distance)

# Display the image with detected dots
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Detected Dots', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def detect_dots(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    dot_positions = []
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            dot_positions.append((x, y))
    return dot_positions

def calculate_pairwise_distances(dot_positions):
    num_dots = len(dot_positions)
    distances = np.zeros((num_dots, num_dots))
    for i in range(num_dots):
        for j in range(i + 1, num_dots):
            distance = calculate_distance(dot_positions[i], dot_positions[j])
            distances[i, j] = distance
            distances[j, i] = distance
    return distances

def calculate_average_pairwise_distance(distances):
    num_dots = distances.shape[0]
    total_distance = np.sum(distances)
    average_distance = total_distance / (num_dots * (num_dots - 1) / 2)
    return average_distance

def main():
    image_path = 'image.jpg'
    dot_positions = detect_dots(image_path)
    distances = calculate_pairwise_distances(dot_positions)
    average_distance = calculate_average_pairwise_distance(distances)
    print("Average Pairwise Distance:", average_distance)
    image = cv2.imread(image_path)
    cv2.drawContours(image, [np.array(dot_positions)], -1, (0, 255, 0), 2)
    cv2.imshow('Detected Dots', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

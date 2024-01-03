import cv2
import numpy as np
import matplotlib.pyplot as plt

#############################################################################################

def shoal_plot():
    image_path = 'shoal_plot.jpg'
    dot_positions = detect_dots(image_path)
    distances = calculate_pairwise_distances(dot_positions)
    average_distance = calculate_average_pairwise_distance(distances)
    print("Average Pairwise Distance:", average_distance)
    image = cv2.imread(image_path)
    cv2.drawContours(image, [np.array(dot_positions)], -1, (0, 255, 0), 2)
    cv2.imshow('Detected Dots', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#############################################################################################

def trajectory_plot(data):
    x = data['X']
    y = data['Y']
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Object Path')
    plt.show()

#############################################################################################

def novel_tank_dive_plot(data, zone_boundaries):
    plt.figure(figsize=(10, 6))
    plt.plot(data['X'], data['Y'], color='blue', label='Path')
    plt.axhline(zone_boundaries[0], color='red', linestyle='--', label='Zone 1')
    plt.axhline(zone_boundaries[1], color='green', linestyle='--', label='Zone 2')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path with Zones')
    plt.legend()

    prev_zone = None

    for index, row in data.iterrows():
        curr_y = row['Y']
        curr_zone = None

        if curr_y <= zone_boundaries[0]:
            curr_zone = 1
        elif curr_y <= zone_boundaries[1]:
            curr_zone = 2
        else:
            curr_zone = 3

        if prev_zone is not None and curr_zone != prev_zone:
            plt.scatter(row['X'], row['Y'], color='black', marker='x')

        prev_zone = curr_zone

    plt.show()

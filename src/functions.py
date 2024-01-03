import cv2
import numpy as np
import math
import pandas as pd

#############################################################################################

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#############################################################################################

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

#############################################################################################

def calculate_pairwise_distances(dot_positions):
    num_dots = len(dot_positions)
    distances = np.zeros((num_dots, num_dots))
    for i in range(num_dots):
        for j in range(i + 1, num_dots):
            distance = calculate_distance(dot_positions[i], dot_positions[j])
            distances[i, j] = distance
            distances[j, i] = distance
    return distances

#############################################################################################

def calculate_average_pairwise_distance(distances):
    num_dots = distances.shape[0]
    total_distance = np.sum(distances)
    average_distance = total_distance / (num_dots * (num_dots - 1) / 2)
    return average_distance

#############################################################################################

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        raise

#############################################################################################

def calculate_path_length(data):
    x = data['X']
    y = data['Y']

    cumulative_length = 0
    prev_x = x.iloc[0]
    prev_y = y.iloc[0]

    for curr_x, curr_y in zip(x[1:], y[1:]):
        distance = math.sqrt((curr_x - prev_x)**2 + (curr_y - prev_y)**2)
        cumulative_length += distance
        prev_x = curr_x
        prev_y = curr_y

    return cumulative_length

#############################################################################################

def calculate_path_zones(data):
    y = data['Y']
    zone_boundaries = define_zones(y)

    zone_1_time = 0
    zone_2_time = 0
    zone_3_time = 0

    prev_zone = None

    for index, row in data.iterrows():
        curr_y = row['Y']
        curr_zone = None

        if curr_y <= zone_boundaries[0]:
            curr_zone = 1
            zone_1_time += row['Time']
        elif curr_y <= zone_boundaries[1]:
            curr_zone = 2
            zone_2_time += row['Time']
        else:
            curr_zone = 3
            zone_3_time += row['Time']

        prev_zone = curr_zone

    return zone_1_time, zone_2_time, zone_3_time

#############################################################################################

def generate_and_save_zones_csv(data, output_csv_path):
    zone_times = calculate_path_zones(data)
    zones_df = pd.DataFrame({
        'Zone': ['Zone 1', 'Zone 2', 'Zone 3'],
        'Time': zone_times
    })
    zones_df.to_csv(output_csv_path, index=False)


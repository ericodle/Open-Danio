import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    """
    Load the CSV file containing the XY pixel positions.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)


def define_zones(y_values):
    """
    Define the zones based on the Y values.

    Args:
        y_values (pd.Series): Series containing the Y values.

    Returns:
        list: List of zone boundaries.
    """
    max_y = y_values.max()
    min_y = y_values.min()
    zone_height = (max_y - min_y) / 3

    zone_boundaries = [min_y + zone_height, min_y + (2 * zone_height)]
    return zone_boundaries


def calculate_path_zones(data):
    """
    Calculate the travel path zones and plot the path with zones overlaid.

    Args:
        data (pd.DataFrame): DataFrame containing the XY pixel positions.

    Returns:
        tuple: A tuple containing the time spent in each zone.
    """
    y = data['Y']
    zone_boundaries = define_zones(y)

    zone_1_time = 0
    zone_2_time = 0
    zone_3_time = 0

    # Plotting the path with zones
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
            zone_1_time += row['Time']
        elif curr_y <= zone_boundaries[1]:
            curr_zone = 2
            zone_2_time += row['Time']
        else:
            curr_zone = 3
            zone_3_time += row['Time']

        if prev_zone is not None and curr_zone != prev_zone:
            plt.scatter(row['X'], row['Y'], color='black', marker='x')

        prev_zone = curr_zone

    plt.show()

    return zone_1_time, zone_2_time, zone_3_time

def calculate_zone_transitions(data):
    """
    Calculate the zone transitions based on the XY coordinate data.

    Args:
        data (pd.DataFrame): DataFrame containing the XY pixel positions.

    Returns:
        dict: Dictionary containing the count of zone transitions.
    """
    y = data['Y']
    zone_boundaries = define_zones(y)

    transitions = {
        'zone1_to_zone2': 0,
        'zone2_to_zone1': 0,
        'zone2_to_zone3': 0,
        'zone3_to_zone2': 0,
        'zone3_to_zone1': 0,
        'zone1_to_zone3': 0,
    }

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

        if prev_zone is not None:
            if curr_zone == 2 and prev_zone == 1:
                transitions['zone1_to_zone2'] += 1
            elif curr_zone == 1 and prev_zone == 2:
                transitions['zone2_to_zone1'] += 1
            elif curr_zone == 3 and prev_zone == 2:
                transitions['zone2_to_zone3'] += 1
            elif curr_zone == 2 and prev_zone == 3:
                transitions['zone3_to_zone2'] += 1
            elif curr_zone == 1 and prev_zone == 3:
                transitions['zone3_to_zone1'] += 1
            elif curr_zone == 3 and prev_zone == 1:
                transitions['zone1_to_zone3'] += 1

        prev_zone = curr_zone

    return transitions

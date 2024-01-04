import csv
import numpy as np

# Set parameters
num_objects = 1   # Number of objects to track
image_height = 1080  # Assuming a 1920x1080 resolution
fps = 30  # Default frames per second

# Define zone boundaries for upper, middle, and bottom thirds
zone_boundaries = [0, image_height // 3, 2 * (image_height // 3), image_height]

# Get user input for the CSV file path
csv_filepath = input("Enter the path to the CSV file for analysis: ")

# Get user input for frames per second
fps_input = input(f"Enter the frames per second (default is {fps}): ")
if fps_input:
    try:
        fps = float(fps_input)
    except ValueError:
        print("Invalid input for frames per second. Using default value.")

# Load data from the CSV file
try:
    data = np.loadtxt(csv_filepath, delimiter=',', skiprows=1)  # Assuming the first row is a header
except FileNotFoundError:
    print(f"Error: The file '{csv_filepath}' was not found.")
    exit()

# Track time spent in each zone and count zone transitions
time_in_zones = [0] * len(zone_boundaries)
zone_transitions = [0] * len(zone_boundaries)  # Updated to include transitions for the last zone

# Function to determine the zone index for a given Y coordinate
def get_zone_index(y):
    for i in range(len(zone_boundaries) - 1):
        if zone_boundaries[i] <= y <= zone_boundaries[i + 1]:
            return i
    return len(zone_boundaries) - 1

# Analyze data
for frame in range(1, len(data)):
    for obj in range(num_objects):
        # Track time in each zone and count zone transitions
        current_zone = get_zone_index(data[frame, obj * 2 + 1])
        previous_zone = get_zone_index(data[frame - 1, obj * 2 + 1])

        time_in_zones[current_zone] += 1

        if current_zone != previous_zone:
            zone_transitions[current_zone] += 1

# Calculate time in seconds
total_seconds = len(data) / fps

# Print time spent in each zone and number of zone transitions
for i in range(len(zone_boundaries) - 1):
    time_in_seconds = time_in_zones[i] / fps
    print(f'Time spent in Zone {i}: {time_in_seconds:.2f} seconds')
    print(f'Number of transitions at Zone {i}: {zone_transitions[i]}')

# Write results to a CSV file
results_filename = 'ntd_analysis_results.csv'
with open(results_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header
    header = ['Zone', 'Time Spent (seconds)', 'Transitions']
    csv_writer.writerow(header)

    # Write data
    for i in range(len(zone_boundaries) - 1):
        csv_writer.writerow([f'Zone {i}', time_in_zones[i] / fps, zone_transitions[i]])

print(f'Analysis results saved to {results_filename}')


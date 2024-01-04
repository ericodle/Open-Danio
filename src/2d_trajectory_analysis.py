import csv
import numpy as np
import matplotlib.pyplot as plt

def calculate_cumulative_path_lengths(data, pixels_per_centimeter=10, frame_rate=30.0):
    centimeters_per_pixel = 1 / pixels_per_centimeter  # Conversion factor

    num_frames, num_coords = data.shape
    num_objects = num_coords // 2

    cumulative_lengths = np.zeros(num_objects)

    for obj in range(num_objects):
        # Extract x and y coordinates for the current object
        x_coords = data[:, obj * 2]
        y_coords = data[:, obj * 2 + 1]

        # Calculate Euclidean distances between consecutive frames in pixels
        distances_pixels = np.sqrt(np.diff(x_coords)**2 + np.diff(y_coords)**2)

        # Convert pixel distances to physical distances in centimeters
        distances_centimeters = distances_pixels * centimeters_per_pixel

        # Calculate cumulative path length (scaled by frame rate)
        cumulative_lengths[obj] = np.sum(distances_centimeters) / frame_rate

    return cumulative_lengths

def plot_object_trajectories(data, pixels_per_centimeter=10):
    centimeters_per_pixel = 1 / pixels_per_centimeter  # Conversion factor

    num_frames, num_coords = data.shape
    num_objects = num_coords // 2

    plt.figure(figsize=(8, 6))

    for obj in range(num_objects):
        # Extract x and y coordinates for the current object
        x_coords = data[:, obj * 2]
        y_coords = data[:, obj * 2 + 1]

        # Convert pixel coordinates to physical coordinates in centimeters
        x_physical = x_coords * centimeters_per_pixel
        y_physical = y_coords * centimeters_per_pixel

        # Plot the trajectory
        plt.plot(x_physical, y_physical, label=f'Object {obj + 1}')

    plt.title('Object Trajectories')
    plt.xlabel('X Position (cm)')
    plt.ylabel('Y Position (cm)')
    plt.legend()
    plt.grid(True)

    # Save the plot to a file (you can choose the file format, e.g., PNG, PDF, SVG, etc.)
    plot_filename = '2d_trajectories.png'
    plt.savefig(plot_filename)
    plt.show()

# Accept CSV file path and pixels per centimeter conversion factor as user input
csv_filepath = input("Enter the path to the CSV file for analysis: ")
pixels_per_centimeter = float(input("Enter the pixels per centimeter conversion factor: "))

try:
    with open(csv_filepath, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Skip the header
        data = np.array([list(map(float, row)) for row in csv_reader])
except FileNotFoundError:
    print(f'Error: File {csv_filepath} not found.')
    exit()

# Calculate cumulative path lengths in centimeters
cumulative_lengths = calculate_cumulative_path_lengths(data, pixels_per_centimeter)

# Display cumulative path lengths for each object in centimeters
for obj, length in enumerate(cumulative_lengths):
    print(f'Object {obj + 1}: Cumulative Path Length = {length:.2f} centimeters')


# Plot trajectories of objects
plot_object_trajectories(data, pixels_per_centimeter)


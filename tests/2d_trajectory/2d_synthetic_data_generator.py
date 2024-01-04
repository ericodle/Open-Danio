import csv
import numpy as np

# Set parameters
num_frames = 10000  # Number of frames
num_objects = 3   # Number of objects to track

# Generate synthetic data
np.random.seed(42)  # Set seed for reproducibility

# Create an array to store the data
data = np.zeros((num_frames, num_objects * 2))  # 2 columns for each object (x and y)

# Generate random starting coordinates for each object
starting_coordinates = np.random.uniform(0, 1920, size=(num_objects, 2))  # assuming a 1920x1080 resolution

# Set the initial coordinates for the first frame
data[0, :] = starting_coordinates.flatten()

# Generate sequential coordinates for each frame
for frame in range(1, num_frames):
    for obj in range(num_objects):
        # Update x and y coordinates for each object based on the previous frame
        delta_x = np.random.uniform(-10, 10)
        delta_y = np.random.uniform(-10, 10)

        # Ensure non-negative coordinates
        new_x = max(0, data[frame - 1, obj * 2] + delta_x)
        new_y = max(0, data[frame - 1, obj * 2 + 1] + delta_y)

        # Add angular velocity for circular motion
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(5, 20)  # Adjust the radius as needed

        data[frame, obj * 2] = new_x + radius * np.cos(angle)
        data[frame, obj * 2 + 1] = new_y + radius * np.sin(angle)

# Save data to a CSV file
csv_filename = 'synthetic_tracking_data_2d.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    header = ['Frame'] + [f'Object_{obj}_X' for obj in range(num_objects)] + [f'Object_{obj}_Y' for obj in range(num_objects)]
    csv_writer.writerow(header)
    
    # Write data
    for frame in range(num_frames):
        row = [frame] + list(data[frame])
        csv_writer.writerow(row)

print(f'Synthetic data with sequential coordinates saved to {csv_filename}')


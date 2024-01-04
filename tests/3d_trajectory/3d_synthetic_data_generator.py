import csv
import numpy as np

def generate_3d_synthetic_data(num_frames, num_objects):
    # Create an array to store the 3D data
    data_3d = np.zeros((num_frames, num_objects * 3))  # 3 columns for each object (x, y, and z)

    # Generate random starting coordinates for each object in 3D space
    starting_coordinates_3d = np.random.uniform(0, 1920, size=(num_objects, 3))  # assuming a 1920x1080x1080 resolution

    # Set the initial coordinates for the first frame
    data_3d[0, :] = starting_coordinates_3d.flatten()

    # Generate sequential coordinates for each frame in 3D
    for frame in range(1, num_frames):
        for obj in range(num_objects):
            # Update x, y, and z coordinates for each object based on the previous frame
            delta_x = np.random.uniform(-10, 10)
            delta_y = np.random.uniform(-10, 10)
            delta_z = np.random.uniform(-10, 10)

            # Ensure non-negative coordinates
            new_x = max(0, data_3d[frame - 1, obj * 3] + delta_x)
            new_y = max(0, data_3d[frame - 1, obj * 3 + 1] + delta_y)
            new_z = max(0, data_3d[frame - 1, obj * 3 + 2] + delta_z)

            # Add angular velocity for circular motion in the xy-plane
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(5, 20)  # Adjust the radius as needed

            data_3d[frame, obj * 3] = new_x + radius * np.cos(angle)
            data_3d[frame, obj * 3 + 1] = new_y + radius * np.sin(angle)
            data_3d[frame, obj * 3 + 2] = new_z

    return data_3d

# Set parameters for 3D data
num_frames_3d = 10000  # Number of frames
num_objects_3d = 3   # Number of objects to track

# Generate 3D synthetic data
np.random.seed(42)  # Set seed for reproducibility
data_3d = generate_3d_synthetic_data(num_frames_3d, num_objects_3d)

# Save 3D data to a CSV file
csv_filename_3d = 'synthetic_tracking_data_3d.csv'
with open(csv_filename_3d, 'w', newline='') as csvfile_3d:
    csv_writer_3d = csv.writer(csvfile_3d)
    
    # Write header
    header_3d = ['Frame'] + [f'Object_{obj}_X' for obj in range(num_objects_3d)] + \
                [f'Object_{obj}_Y' for obj in range(num_objects_3d)] + \
                [f'Object_{obj}_Z' for obj in range(num_objects_3d)]
    csv_writer_3d.writerow(header_3d)
    
    # Write 3D data
    for frame in range(num_frames_3d):
        row_3d = [frame] + list(data_3d[frame])
        csv_writer_3d.writerow(row_3d)

print(f'Synthetic 3D data with sequential coordinates saved to {csv_filename_3d}')


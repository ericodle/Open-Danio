import pandas as pd
import numpy as np

def generate_sample_data(num_frames, num_individuals, image_width, image_height, csv_file_path):
    np.random.seed(42)  # For reproducibility

    data = {'Frame': []}
    for individual_id in range(1, num_individuals + 1):
        data[f'X_Individual_{individual_id}'] = []
        data[f'Y_Individual_{individual_id}'] = []

    for frame in range(1, num_frames + 1):
        data['Frame'].append(frame)
        for individual_id in range(1, num_individuals + 1):
            x_position = np.random.randint(0, image_width)
            y_position = np.random.randint(0, image_height)

            data[f'X_Individual_{individual_id}'].append(x_position)
            data[f'Y_Individual_{individual_id}'].append(y_position)

    # Create DataFrame
    sample_data = pd.DataFrame(data)

    # Save the dataset as a CSV file
    sample_data.to_csv(csv_file_path, index=False)

    print(f"Sample dataset saved to {csv_file_path}")

# User input for parameters
num_frames = int(input("Enter the number of frames: "))
num_individuals = int(input("Enter the number of individuals: "))
image_width = int(input("Enter the image width in pixels: "))
image_height = int(input("Enter the image height in pixels: "))
csv_file_path = input("Enter the path to save the CSV file: ")

# Call the function
generate_sample_data(num_frames, num_individuals, image_width, image_height, csv_file_path)

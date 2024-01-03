# Function to generate sample dataset for multiple individuals
def generate_sample_dataset(num_frames, num_individuals, image_width, image_height):
    np.random.seed(42)  # For reproducibility

    data = {'Frame': [], 'IndividualID': [], 'X': [], 'Y': []}

    for frame in range(1, num_frames + 1):
        for individual_id in range(1, num_individuals + 1):
            x_position = np.random.randint(0, image_width)
            y_position = np.random.randint(0, image_height)

            data['Frame'].append(frame)
            data['IndividualID'].append(individual_id)
            data['X'].append(x_position)
            data['Y'].append(y_position)

    return pd.DataFrame(data)

# User input for parameters
num_frames = int(input("Enter the number of frames: "))
num_individuals = int(input("Enter the number of individuals: "))
image_width = int(input("Enter the image width in pixels: "))
image_height = int(input("Enter the image height in pixels: "))
csv_file_path = input("Enter the path to save the CSV file: ")

# Generate sample dataset for multiple individuals
sample_data = generate_sample_dataset(num_frames, num_individuals, image_width, image_height)

# Save the dataset as a CSV file
sample_data.to_csv(csv_file_path, index=False)

print(f"Sample dataset saved to {csv_file_path}")

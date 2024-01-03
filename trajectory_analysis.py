import src.functions
import src.plotting

def trajectory_analysis():
    image_path = input("Enter the path to the image: ")
    dot_positions = detect_dots(image_path)
    distances = calculate_pairwise_distances(dot_positions)
    average_distance = calculate_average_pairwise_distance(distances)
    print("Average Pairwise Distance:", average_distance)

if __name__ == "__trajectory_analysis__":
    trajectory_analysis()

import src.functions
import src.plotting

def trajectory_analysis():

    # Example usage of CSV functions
    csv_file_path = 'your_data.csv'
    data = load_csv(csv_file_path)
    
    path_length = calculate_path_length(data)
    print("Path Length:", path_length)
    
    trajectory_plot(data)

if __name__ == "__trajectory_analysis__":
    trajectory_analysis()

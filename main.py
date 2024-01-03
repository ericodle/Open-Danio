import src.data_loader
import src.path_analysis
import src.path_visualization

if __name__ == '__main__':
    file_path = input("Enter the path to the CSV file: ")
    data = data_loader.load_csv(file_path)

    path_length = path_analysis.calculate_path_length(data)
    print("Cumulative length of the path:", path_length)

    path_visualization.trace_and_plot_path(data)

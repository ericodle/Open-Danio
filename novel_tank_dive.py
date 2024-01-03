import src.functions
import src.plotting

def novel_tank_dive():

    csv_file_path = 'your_data.csv'
    data = load_csv(csv_file_path)
    path_length = calculate_path_length(data)
    print("Path Length:", path_length)

    zone_times = calculate_path_zones(data)
    print("Zone Times:", zone_times)

    output_csv_path = 'zones_output.csv'
    generate_and_save_zones_csv(data, output_csv_path)

    # Example usage of plotting functions
    trajectory_plot(data)

    zone_boundaries = [50, 100]  # Adjust the zone boundaries as needed
    novel_tank_dive_plot(data, zone_boundaries)

    # Execute the shoal_plot function
    shoal_plot()

if __name__ == "__novel_tank_dive__":
    novel_tank_dive()

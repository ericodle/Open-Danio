import src.functions
import src.plotting

def novel_tank_dive():

    zone_times = calculate_path_zones(data)
    print("Zone Times:", zone_times)

    output_csv_path = 'zones_output.csv'
    generate_and_save_zones_csv(data, output_csv_path)

    zone_boundaries = [50, 100]  # Adjust the zone boundaries as needed
    novel_tank_dive_plot(data, zone_boundaries)

if __name__ == "__novel_tank_dive__":
    novel_tank_dive()

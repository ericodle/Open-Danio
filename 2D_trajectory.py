import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    """
    Load the CSV file containing the XY pixel positions.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)


def trace_and_plot_path(data):
    """
    Trace and plot the object's path using the XY pixel positions.

    Args:
        data (pd.DataFrame): DataFrame containing the XY pixel positions.

    Returns:
        None
    """
    x = data['X']
    y = data['Y']

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Object Path')
    plt.show()


# Usage example
file_path = 'path_data.csv'
data = load_csv(file_path)
trace_and_plot_path(data)
plt.savefig(file_path+'XY_trajectory.tif')

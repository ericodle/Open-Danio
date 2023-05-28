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

def calculate_path_length(data):
    """
    Calculate the cumulative length of the path.

    Args:
        data (pd.DataFrame): DataFrame containing the XY pixel positions.

    Returns:
        float: Cumulative length of the path.
    """
    x = data['X']
    y = data['Y']

    cumulative_length = 0
    prev_x = x.iloc[0]
    prev_y = y.iloc[0]

    for curr_x, curr_y in zip(x[1:], y[1:]):
        distance = math.sqrt((curr_x - prev_x)**2 + (curr_y - prev_y)**2)
        cumulative_length += distance
        prev_x = curr_x
        prev_y = curr_y

    return cumulative_length

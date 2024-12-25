import math

def calculate_standard_deviation(data):
    """
    Standard deviation measures the spread of a data distribution. It measures the typical distance between each data point and the mean.
    :param data: List of numerical values.
    :return: Standard deviation of the dataset.
    """
    all_squared_distances_from_mean = []
    mean = calculate_mean(data)
    for x in data:
        distance_from_mean = x - mean
        distance_from_mean_squared = distance_from_mean * distance_from_mean
        all_squared_distances_from_mean.append(distance_from_mean_squared)
    
    variance = calculate_mean(all_squared_distances_from_mean)
    return math.sqrt(variance)

def calculate_mean(data):
    return sum(data) / len(data)
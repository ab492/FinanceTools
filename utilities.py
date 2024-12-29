import math

def calculate_standard_deviation(data):
    """
    Standard deviation measures the spread of a data distribution. It measures the typical distance between each data point and the mean.
    :param data: List of numerical values.
    :return: Standard deviation of the dataset.
    """
    if not data:
        raise ValueError("The data list cannot be empty")
    else:
        all_squared_distances_from_mean = []
        mean = calculate_mean(data)
        for x in data:
            distance_from_mean = x - mean
            distance_from_mean_squared = distance_from_mean * distance_from_mean
            all_squared_distances_from_mean.append(distance_from_mean_squared)
        
        variance = calculate_mean(all_squared_distances_from_mean)
        return math.sqrt(variance)

def calculate_mean(data):
    if not data:
        raise ValueError("The data list cannot be empty")
    else:
        return sum(data) / len(data)

def calculate_loan_to_value(loan_amount, property_value):
    return (loan_amount / property_value) * 100

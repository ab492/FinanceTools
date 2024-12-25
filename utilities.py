def calculate_standard_deviation(data):
    """
    Standard deviation measures the spread of a data distribution. It measures the typical distance between each data point and the mean.
    :param data: List of numerical values.
    :return: Standard deviation of the dataset.
    """
    if len(data) == 1:
        return 0
    if all(x == data[0] for x in data):
        return 0
    raise NotImplementedError("This function currently handles only single-value or identical-value lists.")

def calculate_mean(data):
    return sum(data) / len(data)
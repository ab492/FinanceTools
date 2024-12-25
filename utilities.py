def calculate_standard_deviation(data):
    """
    Calculate the standard deviation of a dataset.
    :param data: List of numerical values.
    :return: Standard deviation of the dataset.
    """
    if len(data) == 1:
        return 0
    if all(x == data[0] for x in data):
        return 0
    raise NotImplementedError("This function currently handles only single-value or identical-value lists.")
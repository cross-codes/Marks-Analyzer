# gen_stats.py


def nthpercentile(dataframe, marks_column, n):
    """
    Calculate the nth percentile of a specified column in a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - marks_column (str): The column name for which the nth percentile is calculated.
    - n (float): The percentile to calculate (between 0 and 100).

    Returns:
    - float: The nth percentile value for the specified column in the DataFrame.
    """
    return dataframe[marks_column].quantile(n/100)


def generate_stats(dataframe, marks_column, id_column):
    """
    Generate statistics for a specified column in a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - marks_column (str): The column name for which statistics are generated.
    - id_column (str): The column name containing the IDs.

    Returns:
    - tuple: A tuple containing the following statistics:
             (average, median, highest_marks, highest_ID, marks_range).
    """
    average = dataframe[marks_column].mean()
    median = dataframe[marks_column].median()

    highest_ID = dataframe.loc[0, id_column]
    highest_marks = dataframe.loc[0, marks_column]
    lowest_marks = dataframe.loc[len(dataframe.index) - 1, marks_column]

    marks_range = highest_marks - lowest_marks
    return average, median, highest_marks, highest_ID, marks_range


def generate_additional_stats(dataframe, marks_column):
    """
    Generate additional statistics for a specified column in a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - marks_column (str): The column name for which additional statistics are generated.

    Returns:
    - tuple: A tuple containing the following additional statistics:
             (_90_percentile, interquartile_range, standard_deviation).
    """
    _25_percentile = nthpercentile(dataframe, marks_column, 25)
    _75_percentile = nthpercentile(dataframe, marks_column, 75)

    _90_percentile = nthpercentile(dataframe, marks_column, 90)
    iqr = _75_percentile - _25_percentile

    std = dataframe[marks_column].std()

    return _90_percentile, iqr, std

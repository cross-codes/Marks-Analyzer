# gen_stats.py


def nthpercentile(dataframe, marks_column, n):
    return dataframe[marks_column].quantile(n/100)


def generate_stats(dataframe, marks_column, id_column):
    average = dataframe[marks_column].mean()
    median = dataframe[marks_column].median()

    highest_ID = dataframe.loc[0, id_column]
    highest_marks = dataframe.loc[0, marks_column]
    lowest_marks = dataframe.loc[len(dataframe.index) - 1, marks_column]

    marks_range = highest_marks - lowest_marks
    return average, median, highest_marks, highest_ID, marks_range


def generate_additional_stats(dataframe, marks_column):
    _25_percentile = nthpercentile(dataframe, marks_column, 25)
    _75_percentile = nthpercentile(dataframe, marks_column, 75)

    _90_percentile = nthpercentile(dataframe, marks_column, 90)
    iqr = _75_percentile - _25_percentile

    std = dataframe[marks_column].std()

    return _90_percentile, iqr, std

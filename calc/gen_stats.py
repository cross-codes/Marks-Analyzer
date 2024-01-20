# gen_stats.py

def generate_stats(dataframe, marks_column, id_column):
    average = dataframe[marks_column].mean()
    median = dataframe[marks_column].median()
    highest_ID = dataframe.loc[0, id_column]
    highest_marks = dataframe.loc[0, marks_column]
    print(average, median, highest_ID, highest_marks)

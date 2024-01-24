# custom_stats.py

from json import load, JSONDecodeError
from ansi_colors import bcolors


def parse_json(file_name):
    """
    Parse JSON data from a file.

    Parameters:
    - file_name (str): The name of the JSON file to be parsed.

    Returns:
    - dict or None: If successful, returns the parsed JSON data as a dictionary.
                   If the file is not found, prints an error message and returns None.
                   If JSON decoding fails, prints an error message and returns None.
    """
    try:
        with open(file_name, encoding="utf-8") as json_file:
            parsed = load(json_file)
        return parsed
    except FileNotFoundError:
        print(f"{bcolors.BOLD}{bcolors.FAIL}File not found: {
              file_name}{bcolors.ENDC}")
        return None
    except JSONDecodeError:
        print(f"{bcolors.BOLD}{bcolors.FAIL}JSON decoding failed for file: {
              file_name}{bcolors.ENDC}")
        return None


def id_from_name(name, dictionary):
    """
    Retrieve ID and index from a dictionary based on a given name.

    Parameters:
    - name (str): The name to search for in the dictionary.
    - dictionary (dict): A dictionary containing data with the following structure:
                        {index: {'ID': 'some_id', 'alternateNames': ['name1', 'name2', ...]}}

    Returns:
    - tuple or None: If the name is found, returns a tuple containing the ID and the index
                     (ID, index). If the name is not found, returns None.
    """
    for idx in dictionary.items():
        metadata = idx[1]
        if name in metadata["alternateNames"]:
            return metadata["ID"], idx[0]

    return None


def gen_stats_from_id(_id, dataframe, markscolumn, idcolumn, average, highest):
    """
    Generate statistics for a given ID from a DataFrame.

    Parameters:
    - _id (str): The ID for which statistics are to be generated.
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - markscolumn (str): The column name containing the marks data.
    - idcolumn (str): The column name containing the IDs.
    - average (float): The average marks for the entire dataset.
    - highest (float): The highest marks for the entire dataset.

    Returns:
    - tuple or None: If successful, returns a tuple containing four values:
                    (difference from average, difference from highest, rank, marks).
                    If an error occurs during the process, prints an error message,
                    logs the exception, and returns None.
    """
    try:
        row = dataframe[dataframe[idcolumn] == _id]
        rank = dataframe.index[dataframe[idcolumn] == _id].tolist()[0] + 1
        marks = row[markscolumn].values[0]
        return marks - average, highest - marks, rank, marks
    except Exception as e:
        print(e)
        print(f"{bcolors.BOLD}{
              bcolors.FAIL}Statistics generation failed{bcolors.ENDC}")
        return None

# main.py

import argparse
import sys

from ansi_colors import bcolors

try:
    import pandas as pd
    from prettytable import PrettyTable

    from calc.gen_stats import generate_additional_stats, generate_stats
    from calc.histogram import generate_histogram
except ImportError as e:
    print(f"{bcolors.FAIL}{bcolors.BOLD}Error: {
          e}. Please install the required libraries using 'pip install -r requirements.txt'. Is your venv active?{bcolors.ENDC}")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file", help="Name of the .xlsx file to be analyzed. (Must be present in the CWD)")
parser.add_argument("--marksColumn", help="Name of the marks column")
parser.add_argument("--idColumn", help="Name of the ID column")

args = parser.parse_args()


def main():
    SPREADSHEET = args.file
    MARKS_COLUMN = args.marksColumn
    ID_COLUMN = args.idColumn

    # Reading the excel file
    try:
        df = pd.read_excel(SPREADSHEET)
    except FileNotFoundError:
        print(f"{bcolors.FAIL}{bcolors.BOLD}Error: File {
              SPREADSHEET} not found{bcolors.ENDC}")
        sys.exit(1)

    print(
        f"{bcolors.OKGREEN}{bcolors.BOLD}Spreadsheet {
            SPREADSHEET} found and not corrupted  {bcolors.ENDC}",
        end=" "
    )

    if MARKS_COLUMN not in df.columns:
        print(
            f"{bcolors.FAIL}{bcolors.BOLD}Error: Column {
                MARKS_COLUMN} not found in the provided file{bcolors.ENDC}"
        )
        sys.exit(1)

    print(f"{bcolors.OKGREEN}{bcolors.BOLD}Column {
          MARKS_COLUMN} found  {bcolors.ENDC}", end=" ")

    if ID_COLUMN not in df.columns:
        print(
            f"{bcolors.FAIL}{bcolors.BOLD}Error: Column {
                ID_COLUMN} not found in the provided file{bcolors.ENDC}"
        )
        sys.exit(1)

    print(f"{bcolors.OKGREEN}{bcolors.BOLD}Column {
          ID_COLUMN} found  {bcolors.ENDC}")

    # Sorting the dataframe
    df = df.sort_values(by=MARKS_COLUMN, ascending=False)

    # Generating general class statistics
    average, median, highest_marks, highest_ID, marks_range = generate_stats(
        df, MARKS_COLUMN, ID_COLUMN)

    # Display general statistics
    table = PrettyTable(
        ["Average", "Median", "Range", "Highest Marks", "Topper"])
    table.add_row([round(average, 2), round(median, 2), round(
        marks_range, 1), round(highest_marks, 1), highest_ID])
    print(table)

    # Prompt for additional statistics
    print("Display additional statistics? Enter 1 for yes and 0 for no: ",
          end="", flush=True)
    try:
        display_additional = int(sys.stdin.readline())
    except ValueError:
        print("Invalid input entered")
        sys.exit(1)

    if (display_additional == 1):
        _90_pr, iqr, std = generate_additional_stats(df, MARKS_COLUMN)
        add_table = PrettyTable(
            ["90th percentile", "Interquartile Range", "Standard deviation"])
        add_table.add_row([round(_90_pr, 2), round(iqr, 2), round(std, 2)])
        print(add_table)

    # Generate histogram
    try:
        generate_histogram(df, MARKS_COLUMN)
        print(f"{bcolors.BOLD}{bcolors.OKGREEN} Histogram created for {
              SPREADSHEET} in '_plots/'  {bcolors.ENDC}")
    except Exception as _:
        print(f"{bcolors.BOLD}{
              bcolors.FAIL} Histogram generation failed {bcolors.ENDC}")


if __name__ == "__main__":
    if not args.file or not args.marksColumn or not args.idColumn:
        print(f"{bcolors.WARNING}{
              bcolors.BOLD}Insufficient arguments supplied. Refer to --help to see which arguments need to be specified{bcolors.ENDC}")
    else:
        main()

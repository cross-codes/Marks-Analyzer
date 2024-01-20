# main.py

import argparse
import sys

from calc.gen_stats import generate_stats


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


try:
    import pandas as pd
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

    try:
        df = pd.read_excel(SPREADSHEET)
    except FileNotFoundError:
        print(f"{bcolors.FAIL}{bcolors.BOLD}Error: File {
              SPREADSHEET} not found{bcolors.ENDC}")
        sys.exit(1)

    print(
        f"{bcolors.OKGREEN}{bcolors.BOLD}Spreadsheet {
            SPREADSHEET} found and not corrupted ...{bcolors.ENDC}"
    )

    if MARKS_COLUMN not in df.columns:
        print(
            f"{bcolors.FAIL}{bcolors.BOLD}Error: Column {
                MARKS_COLUMN} not found in the provided file{bcolors.ENDC}"
        )
        sys.exit(1)

    print(f"{bcolors.OKGREEN}{bcolors.BOLD}Column {
          MARKS_COLUMN} found ...{bcolors.ENDC}")

    if ID_COLUMN not in df.columns:
        print(
            f"{bcolors.FAIL}{bcolors.BOLD}Error: Column {
                ID_COLUMN} not found in the provided file{bcolors.ENDC}"
        )
        sys.exit(1)

    print(f"{bcolors.OKGREEN}{bcolors.BOLD}Column {
          ID_COLUMN} found ...{bcolors.ENDC}")

    df = df.sort_values(by=MARKS_COLUMN, ascending=False)
    generate_stats(df, MARKS_COLUMN, ID_COLUMN)


if __name__ == "__main__":
    if not args.file or not args.marksColumn or not args.idColumn:
        print(f"{bcolors.WARNING}{
              bcolors.BOLD}Insufficient arguments supplied. Refer to --help to see which arguments need to be specified{bcolors.ENDC}")
    else:
        main()

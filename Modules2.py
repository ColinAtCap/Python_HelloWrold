
#csv module provides functionality to read and write CSV files.

import csv
def read_csv(file_path):
    """
    Reads a CSV file and returns its content as a list of dictionaries.
    
    :param file_path: Path to the CSV file.
    :return: List of dictionaries representing the CSV rows.
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
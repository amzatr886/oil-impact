import pandas as pd


def loader_dataFrame(file_path):
    dt = pd.read_csv(file_path)
    return dt


# Newline to separate the two functions

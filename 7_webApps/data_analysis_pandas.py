import pandas as pd


class DataAnalysis:
    def __init__(self,csv_file_path):
        self.df = pd.read_csv(csv_file_path)


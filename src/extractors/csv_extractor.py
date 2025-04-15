import os
import pandas as pd
from typing import List
from .base_extractor import BaseExtractor


class CsvExtractor(BaseExtractor):
    
    #constructor
    def __init__(self, file_paths: List[str]):
        self.file_paths = file_paths


    #method
    def extract(self) -> pd.DataFrame:

        dfs = []  # List to store individual DataFrames
        
        for file_path in self.file_paths:
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)  # Load the CSV
                dfs.append(df)  # Append it to the list
        
        # Combine all DataFrames into one if you want
        combined_df = pd.concat(dfs, ignore_index=True)
        
        return combined_df
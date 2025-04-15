import os
import pandas as pd
from typing import Dict
from .base_extractor import BaseExtractor


class CsvExtractor(BaseExtractor):
    
    def __init__(self, file_paths: Dict[str, str]):
        self.file_paths = file_paths  # Dictionary like {"product": "E:/.../product.csv", ...}

    def extract(self) -> Dict[str, pd.DataFrame]:
        dataframes = {}

        for key, path in self.file_paths.items():
            if os.path.exists(path):
                df = pd.read_csv(path)
                dataframes[key] = df
            else:
                print(f"File not found: {path}")
        
        return dataframes
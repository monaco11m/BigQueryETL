from google.cloud import storage
import pandas as pd
import os
from typing import Dict
from .base_extractor import BaseExtractor
from io import StringIO

class CsvExtractor(BaseExtractor):

    def __init__(self, file_paths: Dict[str, str]):
        self.file_paths = file_paths

    def extract(self) -> Dict[str, pd.DataFrame]:
        dfs = {}
        client = storage.Client()

        for key, path in self.file_paths.items():
            if path.startswith("gs://"): #Detects if is reading from GCS instead of local files
                # Extract bucket and file path
                bucket_name = path.split("/")[2]
                file_path = "/".join(path.split("/")[3:])

                # Download file content from GCS
                bucket = client.bucket(bucket_name)
                blob = bucket.blob(file_path)
                content = blob.download_as_text()

                # Convert CSV string to DataFrame
                dfs[key] = pd.read_csv(StringIO(content))
            else:
                # local files
                if os.path.exists(path):
                    dfs[key] = pd.read_csv(path)
                else:
                    print(f"File not found: {path}")

        return dfs

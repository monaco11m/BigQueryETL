import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from .base_loader import BaseLoader
import config  
import os

class BigQueryLoader(BaseLoader):
    def __init__(self):
        # Try to use local credentials (.json) if they are defined or if the file exists
        if (
            hasattr(config, "GOOGLE_CREDENTIALS_PATH") and 
            config.GOOGLE_CREDENTIALS_PATH and 
            os.path.exists(config.GOOGLE_CREDENTIALS_PATH)
        ):
            credentials_bigQuery = service_account.Credentials.from_service_account_file(
                config.GOOGLE_CREDENTIALS_PATH
            )
            self.client = bigquery.Client(credentials=credentials_bigQuery, project=config.BQ_PROJECT_ID)
        else:
            # if there is no local credential file, it means its executing by GCP then use default credentials
            self.client = bigquery.Client(project=config.BQ_PROJECT_ID)


    def load(self, df: pd.DataFrame, table_name: str) -> None:
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE, #Other options could be WRITE_APPEND (add to existing) or WRITE_EMPTY (only write if table is empty).
            autodetect=True, #This tells BigQuery to automatically detect the schema (data types of columns) based on the DataFrame.
        )

        job = self.client.load_table_from_dataframe(
            df, table_name, job_config=job_config
        )
        job.result()  # wait until job is finished

        print(f"Loaded {len(df)} rows into {table_name}")

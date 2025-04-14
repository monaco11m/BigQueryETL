import pandas as pd
from google.cloud import bigquery
import os

# 1. Google credentials path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"E:\ETL\BigQueryETL\etlproject-456806-e2f687607c74.json"  

# 2. BigQuery setup
project_id = "etlproject-456806"        # Replace with your actual project ID
dataset_id = "my_dataset"             # Replace with your dataset name
table_id = "products"                 

# 3. Load CSV file
csv_path = r"C:\Users\usuario\Downloads\Kaggle\olist_products_dataset.csv"
df = pd.read_csv(csv_path)

# 4. (Optional) Transform
df.dropna(inplace=True)

# 5. Upload to BigQuery
client = bigquery.Client(project=project_id)
table_ref = f"{project_id}.{dataset_id}.{table_id}"

job = client.load_table_from_dataframe(df, table_ref)
job.result()

print(f"✅ Data uploaded successfully to {table_ref}")

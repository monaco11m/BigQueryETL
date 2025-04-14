# config.py

# CSV files
PRODUCT_CSV_PATH = r"E:\ETL\BigQueryETL\data\olist_products_dataset.csv"
CUSTOMER_CSV_PATH = r"E:\ETL\BigQueryETL\data\olist_customers_dataset.csv"

# Google BigQuery configuration
BQ_PROJECT_ID = "etlproject-456806"
BQ_DATASET_ID = "my_dataset"

# Fully-qualified BigQuery table names
BQ_PRODUCT_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.products"
BQ_CUSTOMER_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.customers"

# Credentials JSON path
GOOGLE_CREDENTIALS_PATH = r"E:\ETL\BigQueryETL\etlproject-456806-e2f687607c74.json"

# config.py

# CSV files
PRODUCT_CSV_PATH = r"E:\ETL\BigQueryETL\data\product.csv"
CUSTOMER_CSV_PATH = r"E:\ETL\BigQueryETL\data\customer.csv"
ORDER_CSV_PATH = r"E:\ETL\BigQueryETL\data\order.csv"
ORDERDETAIL_CSV_PATH = r"E:\ETL\BigQueryETL\data\order_detail.csv"
SELLER_CSV_PATH = r"E:\ETL\BigQueryETL\data\seller.csv"


DATA_PATHS = {
    "product": PRODUCT_CSV_PATH,
    "customer": CUSTOMER_CSV_PATH,
    "order": ORDER_CSV_PATH,
    "order_detail": ORDERDETAIL_CSV_PATH,
    "seller": SELLER_CSV_PATH
}


# Google BigQuery configuration
BQ_PROJECT_ID = "etlproject-456806"
BQ_DATASET_ID = "my_dataset"

# Fully-qualified BigQuery table names
BQ_PRODUCT_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.products"
BQ_CUSTOMER_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.customers"

# Credentials JSON path
GOOGLE_CREDENTIALS_PATH = r"E:\ETL\BigQueryETL\credentials\etlproject-456806-e2f687607c74.json"

import os
from dotenv import load_dotenv

# CSV files
PRODUCT_CSV_PATH = "gs://kaggle-dataset-raw/data/product.csv"
CUSTOMER_CSV_PATH = "gs://kaggle-dataset-raw/data/customer.csv"
ORDER_CSV_PATH = "gs://kaggle-dataset-raw/data/order.csv"
ORDERDETAIL_CSV_PATH = "gs://kaggle-dataset-raw/data/order_detail.csv"
SELLER_CSV_PATH = "gs://kaggle-dataset-raw/data/seller.csv"


DATA_PATHS = {
    "product": PRODUCT_CSV_PATH,
    "customer": CUSTOMER_CSV_PATH,
    "order": ORDER_CSV_PATH,
    "order_detail": ORDERDETAIL_CSV_PATH,
    "seller": SELLER_CSV_PATH
}

load_dotenv()

# Google BigQuery configuration
BQ_PROJECT_ID = os.getenv("BQ_PROJECT_ID")
BQ_DATASET_ID = os.getenv("BQ_DATASET_ID")
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")

# Fully-qualified BigQuery table names
BQ_PRODUCT_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.dim_product"
BQ_CUSTOMER_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.dim_customer"
BQ_SELLER_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.dim_seller"
BQ_ORDER_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.dim_order"
BQ_ORDER_DETAIL_TABLE = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.fact_order_detail"



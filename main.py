import pandas as pd
from src.extract import CsvExtractor
from src.transform import ProductTransformer
from src.transform import SellerTransformer
from src.transform import CustomerTransformer
from src.transform import OrderTransformer
from src.load import BigQueryLoader
import config

def main():
    # EXTRACT
    extractor = CsvExtractor(file_paths=config.DATA_PATHS)
    dfs = extractor.extract()
    product_df = dfs["product"]
    seller_df = dfs["seller"]
    customer_df = dfs["customer"]
    order_df = dfs["order"]

    # TRANSFORM
    transformer_product = ProductTransformer()
    transformed_product_df = transformer_product.transform(product_df)

    transformer_seller = SellerTransformer()
    transformed_seller_df = transformer_seller.transform(seller_df)

    transformer_customer = CustomerTransformer()
    transformed_customer_df = transformer_customer.transform(customer_df)

    transformer_order = OrderTransformer()
    transformed_order_df = transformer_order.transform(order_df)

    # LOAD
    loader = BigQueryLoader()
    loader.load(transformed_product_df, config.BQ_PRODUCT_TABLE)

if __name__ == "__main__":
    main()

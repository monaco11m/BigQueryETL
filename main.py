import pandas as pd
from src.extract import CsvExtractor
from src.transform import ProductTransformer
from src.transform import SellerTransformer
from src.transform import CustomerTransformer
from src.transform import OrderTransformer
from src.transform import OrderDetailTransformer
from src.load import BigQueryLoader
from src.fact_builders import OrderDetailFactBuilder

import config

def main():
    # EXTRACT
    extractor = CsvExtractor(file_paths=config.DATA_PATHS)
    dfs = extractor.extract()
    product_df = dfs["product"]
    seller_df = dfs["seller"]
    customer_df = dfs["customer"]
    order_df = dfs["order"]
    order_detail_df = dfs["order_detail"]

    # TRANSFORM
    transformer_product = ProductTransformer()
    transformed_product_df = transformer_product.transform(product_df)

    transformer_seller = SellerTransformer()
    transformed_seller_df = transformer_seller.transform(seller_df)

    transformer_customer = CustomerTransformer()
    transformed_customer_df = transformer_customer.transform(customer_df)

    transformer_order = OrderTransformer()
    transformed_order_df = transformer_order.transform(order_df)

    transformer_order_detail = OrderDetailTransformer()
    transformed_order_detail_df = transformer_order_detail.transform(order_detail_df)

    fact_builder = OrderDetailFactBuilder(transformed_order_detail_df, transformed_order_df)
    fact_order_detail_df = fact_builder.build()

    # LOAD
    loader = BigQueryLoader()
    loader.load(transformed_product_df, config.BQ_PRODUCT_TABLE)
    loader.load(transformed_seller_df, config.BQ_SELLER_TABLE)
    loader.load(transformed_customer_df, config.BQ_CUSTOMER_TABLE)
    loader.load(transformed_order_df, config.BQ_ORDER_TABLE)
    loader.load(fact_order_detail_df, config.BQ_ORDER_DETAIL_TABLE)

if __name__ == "__main__":
    main()


def run_etl(event, context):
    main()
import pandas as pd
from src.extract import CsvExtractor
from src.transform import ProductTransformer
from src.load import BigQueryLoader
import config

def main():
    # EXTRACT
    extractor = CsvExtractor(file_paths=config.DATA_PATHS)
    dfs = extractor.extract()
    product_df = dfs["product"]

    # TRANSFORM
    transformer = ProductTransformer()
    transformed_product_df = transformer.transform(product_df)

    # LOAD
    loader = BigQueryLoader()
    loader.load(transformed_product_df, config.BQ_PRODUCT_TABLE)

if __name__ == "__main__":
    main()

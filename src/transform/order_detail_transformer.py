import pandas as pd
from .base_transformer import BaseTransformer

class OrderDetailTransformer(BaseTransformer):  

    def transform(self, df:pd.DataFrame)->pd.DataFrame:

        decimal_columns = ['price', 'freight_value']
        df.replace("",pd.NA,inplace=True)


        df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'], errors='coerce')
        df['order_item_id'] = pd.to_numeric(df['order_item_id'], errors='coerce')
        for col in decimal_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        

        df = df.dropna(how="all")

        #define order_item_id as int
        df['order_item_id'] = df['order_item_id'].astype(int)
        df['price'] = df['price'].round(2)
        df['freight_value'] = df['freight_value'].round(2)
        

        return df
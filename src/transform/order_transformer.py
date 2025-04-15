import pandas as pd
from base_transformer import BaseTransformer

class OrderTransformer(BaseTransformer):

    def transform(self, df:pd.DataFrame)->pd.DataFrame:
        
        df.replace("",pd.NA,inplace=True)
        df = df.dropna(how=all)

        #rename old, new
        df = df.rename(columns={
            "order_purchase_timestamp","order_purchase_date",
            "order_approved_at","order_approved_date"
        })

        datetime_columns = ["order_purchase_date", "order_approved_date", "order_delivered_carrier_date", "order_delivered_customer_date","order_estimated_delivery_date"]

        #validation for all columns define as datetime
        for col in datetime_columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

        # delete rows where *any* of these datetime fields failed to convert
        df = df.dropna(subset=datetime_columns)
        
        return df
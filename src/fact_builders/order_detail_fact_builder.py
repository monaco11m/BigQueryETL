import pandas as pd

class OrderDetailFactBuilder :

    def __init__(self,order_detail_df,order_df):
        self.order_detail_df=order_detail_df
        self.order_df=order_detail_df


    def build(self)->pd.DataFrame:

        df_merged=self.order_detail_df.copy()

        # Merge with orders_df to get customer_id
        df_merged = df_merged.merge(self.orders_df[['order_id', 'customer_id']], on='order_id', how='left')
        
        #sort columns
        df = df[['order_id', 'order_item_id', 'product_id', 'seller_id', 'customer_id', 'shipping_limit_date', 'price', 'freight_value']]
        
        return df

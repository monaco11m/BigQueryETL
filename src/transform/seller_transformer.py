import pandas as pd
from .base_transformer import BaseTransformer

class SellerTransformer(BaseTransformer):
    
    def transform(self, df:pd.DataFrame) -> pd.DataFrame:
        
        df.replace("",pd.NA,inplace=True)
        df = df.dropna(how="all")

        #rename old_name : new_name

        df = df.rename(columns={
            "seller_zip_code_prefix" : "seller_zip_code"
        })

        df["seller_zip_code"] = pd.to_numeric(df["seller_zip_code"],errors="coerce").fillna(0).astype(int)

        return df

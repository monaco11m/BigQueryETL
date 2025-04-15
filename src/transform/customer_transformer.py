import pandas as pd
from .base_transformer import BaseTransformer

class SellerTransformer(BaseTransformer):
    
    def transform(self, df:pd.DataFrame) -> pd.DataFrame:

        df.replace("",pd.NA,inplace=True)
        df = df.dropna(how=all)

        #rename
        df = df.rename(columns={
            "customer_zip_code_prefix","customer_zip_code"
        })
        
        df["customer_zip_code"] = pd.to_numeric(df["customer_zip_code"],errors="coerce").fillna(0).astype(int)

        return df
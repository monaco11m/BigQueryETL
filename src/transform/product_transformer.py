import pandas as pd
from .base_transformer import BaseTransformer

class ProductTransformer(BaseTransformer):
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        
        # empty cell is not the same as NaN value so if you want to avoid "" cells, you should do this
        df.replace("", pd.NA, inplace=True)

        # avoid cells if contains NaN  values
        df = df.dropna(subset=["product_id", "product_category_name", "product_name_lenght", "product_photos_qty", "product_weight_g", 
                               "product_length_cm", "product_height_cm","product_width_cm",])
        #use df = df.dropna(how='all') if you want to remove all missing data



        # rename columns old : new
        df = df.rename(columns={
            "product_category_name": "product_name",
            "product_weight_g": "product_weight",
            "product_length_cm": "product_length",
            "product_height_cm": "product_height",
            "product_width_cm": "product_width"
        })

        # validate datatype, fillna = 0 => if the value is not float set 0

        df["product_weight"] = pd.to_numeric(df["product_weight"], errors="coerce").fillna(0).astype(float)
        df["product_length"] = pd.to_numeric(df["product_length"], errors="coerce").fillna(0).astype(float)
        df["product_height"] = pd.to_numeric(df["product_height"], errors="coerce").fillna(0).astype(float)
        df["product_width"] = pd.to_numeric(df["product_width"], errors="coerce").fillna(0).astype(float)
        
        return df

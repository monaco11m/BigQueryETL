import pandas as pd
from src.transform.order_transformer import OrderTransformer

def test_order_transformer_drop_all_invalid_or_partial_row():

    df = pd.DataFrame({
        "order_purchase_timestamp": ["2025-01-01 10:00", "invalid_date"],
        "order_approved_at": ["2025-01-01 11:00", "invalid_date"],
        "order_delivered_carrier_date": [None, None],
        "order_delivered_customer_date": [None, None],
        "order_estimated_delivery_date": [None, None],
    })

    transformer = OrderTransformer()
    transformed_df = transformer.transform(df)

    # All rows should be dropped due to missing datetime fields
    assert transformed_df.empty


def test_order_transformer_renames_columns():

    df = pd.DataFrame({
        "order_purchase_timestamp": ["2025-01-01 10:00", "2025-01-02 11:00"],
        "order_approved_at": ["2025-01-01 11:00", "2025-01-02 12:00"],
        "order_delivered_carrier_date": [None, None],
        "order_delivered_customer_date": [None, None],
        "order_estimated_delivery_date": [None, None],
    })
    
    transformer = OrderTransformer()
    transformed_df = transformer.transform(df)

    assert "order_purchase_date" in transformed_df.columns
    assert "order_approved_date" in transformed_df.columns
    assert "order_purchase_timestamp" not in transformed_df.columns
    assert "order_approved_at" not in transformed_df.columns


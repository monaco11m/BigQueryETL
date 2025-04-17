import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
from src.load.bigquery_loader import BigQueryLoader

@patch("src.load.bigquery_loader.bigquery.Client")
@patch("src.load.bigquery_loader.service_account.Credentials")
def test_bigquery_loader_load(mock_credentials, mock_bigquery_client):
    # Arrange
    mock_client_instance = MagicMock()
    mock_bigquery_client.return_value = mock_client_instance
    mock_job = MagicMock()
    mock_client_instance.load_table_from_dataframe.return_value = mock_job
    
    loader = BigQueryLoader()

    df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    table_name = "project.dataset.table"

    # Act
    with patch("builtins.print") as mock_print:
        loader.load(df, table_name)

    # Assert
    mock_client_instance.load_table_from_dataframe.assert_called_once()
    args, kwargs = mock_client_instance.load_table_from_dataframe.call_args
    assert args[0].equals(df)
    assert args[1] == table_name

    mock_job.result.assert_called_once()
    mock_print.assert_called_once_with(f"Loaded {len(df)} rows into {table_name}")

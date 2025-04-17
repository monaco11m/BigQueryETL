from unittest.mock import MagicMock, patch
import pandas as pd
from src.load.bigquery_loader import BigQueryLoader

#These decorators replace bigquery.Client and service_account.Credentials with mock objects during the test
@patch("src.load.bigquery_loader.bigquery.Client")
@patch("src.load.bigquery_loader.service_account.Credentials")
def test_bigquery_loader_load(mock_credentials, mock_bigquery_client):

    mock_client_instance = MagicMock()
    mock_bigquery_client.return_value = mock_client_instance
    mock_job = MagicMock()

    # When load_table_from_dataframe() is called, it will return this mock_job,which has a fake result() function.
    mock_client_instance.load_table_from_dataframe.return_value = mock_job
  
    loader = BigQueryLoader()

    df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    table_name = "project.dataset.table"

    # this mocking print() just for test that the message gets printed correctly.
    with patch("builtins.print") as mock_print:
        loader.load(df, table_name)

    # Assert
    # Make sure the load_table_from_dataframe function was called exactly once.
    mock_client_instance.load_table_from_dataframe.assert_called_once()

    args, kwargs = mock_client_instance.load_table_from_dataframe.call_args
    assert args[0].equals(df) # first arg: DataFrame
    assert args[1] == table_name # second arg: table name

    # Ensure .result() was called on the returned job
    mock_job.result.assert_called_once()

    # Verify that the success message was printed.
    mock_print.assert_called_once_with(f"Loaded {len(df)} rows into {table_name}")

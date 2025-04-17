import pandas as pd
from unittest.mock import patch
from src.extract.csv_extractor import CsvExtractor

def test_csv_extractor_with_valid_path():

    # create a a dictionary with key and path
    mock_path = {"product": "fake/path/product.csv"}

    # create a dataFrame
    mock_df = pd.DataFrame({"id": [1, 2], "name": ["A", "B"]})

    #This replaces os.path.exists() just during the test with a function that always returns True.
    #So we can simulate that the file exists, without actually needing a real file on disk.
    with patch("src.extract.csv_extractor.os.path.exists", return_value=True), \
        patch("src.extract.csv_extractor.pd.read_csv", return_value=mock_df):
        #This replaces pd.read_csv() with a fake function that always returns mock_df.
        #So we can simulate that the file exists, without actually needing a real file on disk.
        
        extractor = CsvExtractor(mock_path)
        result = extractor.extract()

        assert "product" in result #Did the extractor return a DataFrame with the key "product"?
        pd.testing.assert_frame_equal(result["product"], mock_df)#Is the DataFrame under "product" exactly equal to the mocked one we expected?


    #output : "." is success, if faied then "F"
    #pytest -v for more detail
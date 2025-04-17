import pandas as pd
from unittest.mock import patch
from src.extract.csv_extractor import CsvExtractor

#output : "." is success, if faied then "F"
#pytest -v for more detail

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


def test_csv_extractor_file_not_found(capfd):

    file_paths = {"product": "fake_path/product.csv"}
    extractor = CsvExtractor(file_paths)

    result = extractor.extract()

    # No DataFrame 
    assert "product" not in result

    # Check printed output
    # out capture the error message and will validate if contains "File not found: fake_path/product.csv" exists in error message
    out, _ = capfd.readouterr()
    assert "File not found: fake_path/product.csv" in out


def test_csv_extractor_empty_paths():
    extractor = CsvExtractor({})
    result = extractor.extract()

    #Checks that the extract() method returns an empty dictionary if file_paths is an empty dictionary too. If there's nothing to extract, the output should be an empty dict
    assert result == {}

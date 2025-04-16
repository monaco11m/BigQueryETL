# BigQuery ETL Project

This project implements an ETL (Extract, Transform, Load) pipeline using Python to extract data from CSV files, transform it, and load it into Google BigQuery.

## Project Structure

- `src/`: Contains the main code for transforming and processing the data.
  - `transform/`: Folder where the transformation classes are located.
  - `fact_builders/`: Contains logic to build the fact tables.
  - `base_transformer.py`: Base class for all transformers.
- `config.py`: Configuration file that includes paths to the input files and credentials for BigQuery.
- `main.py`: The entry point for running the ETL pipeline.
- `requirements.txt`: Lists the Python dependencies for the project.
- `.gitignore`: Specifies files and directories that should be ignored by Git (e.g., credentials, environment files).

## How to Run

1. Clone this repository.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   
3. Make sure you have a .env file with the required environment variables, including the path to your Google BigQuery credentials.

4. Run the ETL process:
   python main.py

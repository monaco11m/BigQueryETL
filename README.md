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


## 🚀 How to Run This Project

Follow these steps to set up and run the ETL locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate a Virtual Environment

#### Windows (PowerShell):

```bash
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
```

#### Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root of the project with the following content:

```env
BQ_PROJECT_ID=your_project_id
BQ_DATASET_ID=dwh_dataset
GOOGLE_CREDENTIALS_PATH=E:/ETL/BigQueryETL/credentials/your-service-account.json
```

✅ Your .env and credentials/ folder are already included in .gitignore.

### 5. Run the ETL Pipeline

```bash
python main.py
```

---

## ✅ Notes

- Make sure your credentials JSON file is not tracked by Git.
- All sensitive info should go in the `.env` file (already in `.gitignore`).


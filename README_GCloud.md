# Google Cloud Deployment Guide for BigQueryETL

This document explains how to prepare, configure, and deploy your ETL pipeline using Google Cloud Platform (GCP), step by step. It assumes you are working with a project that extracts CSV data, transforms it, and loads it into BigQuery.

---

## ☁️ Prerequisites

- Google Cloud account: https://console.cloud.google.com/
- Python 3.8+
- `gcloud` CLI installed: https://cloud.google.com/sdk/docs/install
- `gsutil` tool (included in `gcloud`)

---

## 🔑 1. Authenticate with Google Cloud

```bash
gcloud auth login
```
- A browser window will open — sign in with your Google account.

Then set your project:
```bash
gcloud config set project <your-project-id>
```
Example:
```bash
gcloud config set project kaggeetl
```

---

## 🪣 2. Create a Cloud Storage Bucket

Go to https://console.cloud.google.com/storage and create a new bucket:

- Name: `kaggle-dataset-raw`
- Location: your preferred region (e.g., `us-central1`)
- Access Control: Uniform
- Uncheck "Enforce public access prevention" (if you want flexibility for sharing)

---

## 🗃️ 3. Upload Your CSV Files to the Bucket

From your terminal:
```bash
cd E:/ETL/BigQueryETL/data

# Upload each file
gsutil cp product.csv gs://kaggle-dataset-raw/data/product.csv
gsutil cp customer.csv gs://kaggle-dataset-raw/data/customer.csv
gsutil cp order.csv gs://kaggle-dataset-raw/data/order.csv
gsutil cp order_detail.csv gs://kaggle-dataset-raw/data/order_detail.csv
gsutil cp seller.csv gs://kaggle-dataset-raw/data/seller.csv
```

---

## 🔒 4. Grant Access to BigQuery and Storage

### Enable the following APIs in your project:
- BigQuery API
- Cloud Storage API

Visit: https://console.cloud.google.com/apis/library

### Add IAM Roles:
From the IAM section:
- Grant the following roles to your user or service account:
  - BigQuery Admin
  - Storage Admin

---

## 🧠 5. Set Up Application Default Credentials (ADC)

```bash
gcloud auth application-default login
```
This will allow Python libraries (like `google-cloud-storage`) to access GCP.

---

## 📦 6. Install Required Python Packages

Inside your virtual environment:
```bash
pip install -r requirements.txt
```
Make sure `google-cloud-storage` and `google-cloud-bigquery` are listed.

---

## 🧪 7. Test the Process

Make sure your `config.py` is updated with the GCS paths like:
```python
PRODUCT_CSV_PATH = 'gs://kaggle-dataset-raw/data/product.csv'
```
Then run:
```bash
python main.py
```

---

## 💡 Notes

- `.gcloudignore` helps you avoid uploading unnecessary files like `.git/`, `node_modules/`, etc.
- Use environment variables for sensitive configs (optional)
- Consider Cloud Scheduler or Cloud Functions to automate the process

---

## 📄 PDF Version
A PDF version of this guide is available in the `/docs` folder: `docs/gcloud_deployment_guide.pdf`

---

Happy deploying 🚀


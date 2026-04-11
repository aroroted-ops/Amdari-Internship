# Architecture Diagram

This repository implements a simple cloud-native ELT pipeline using AWS S3, Airbyte, MotherDuck, Python, and Boto3.

## Pipeline summary

- Raw CSV files begin in the local `dataset/` directory.
- `upload_s3.py` uploads those files to an S3 bucket using `boto3`.
- Airbyte connects to the S3 bucket as a source.
- Airbyte syncs the raw data into MotherDuck.
- MotherDuck stores the ingested data and makes it available for SQL queries.

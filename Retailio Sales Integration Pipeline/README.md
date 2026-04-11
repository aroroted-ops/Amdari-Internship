# Amdari Internship

## Cloud-native ELT pipeline

This repository demonstrates a cloud-native ELT pipeline using:

- **AWS S3** for raw data storage
- **Airbyte** for data integration and ingestion
- **MotherDuck** as the analytics warehouse
- **Python** and **Boto3** for uploading raw data to S3

The workflow is:

1. Raw CSV files are stored locally in the `dataset/` folder.
2. `upload_s3.py` uploads those files into an S3 bucket.
3. Airbyte is configured with an S3 source connector.
4. Airbyte loads the data into MotherDuck.
5. Data is queried in MotherDuck for analysis.

## Repository contents

- `upload_s3.py` - Python script that uploads dataset files from `dataset/` to S3 using `boto3`.
- `dataset/` - Raw CSV dataset files loaded into the pipeline.
- `sql-codes.sql` - SQL queries used to explore the data in MotherDuck.
- `ARCHITECTURE.md` - Architecture diagram and ELT flow summary.
- `Airbyte connection.png` - Screenshot of the Airbyte connection setup.
- `MotherDuck customer_V2 query.png`, `MotherDuck product_V2 query.png`, `MotherDuck sales_V2 query.png` - Examples of query results from MotherDuck.

## Tools used

- **AWS S3** as the landing zone for raw dataset files.
- **Airbyte** to connect S3 as a source and MotherDuck as a destination.
- **MotherDuck** to store and query the ingested data.
- **Python** for scripting the upload process.
- **Boto3** for AWS S3 operations.

## How it works

- Raw CSV data is prepared in the `dataset/` folder.
- The upload script sends the files to S3.
- Airbyte reads the raw data from S3 and writes it into MotherDuck.
- SQL queries are executed in MotherDuck to validate, analyze, and report on the loaded data.

## Getting started

1. Ensure AWS credentials are configured locally.
2. Update `upload_s3.py` with your S3 bucket and file name.
3. Run the script:

```bash
python upload_s3.py
```

4. In Airbyte, create an S3 source connector and a MotherDuck destination connector.
5. Run the Airbyte sync to load data into MotherDuck.
6. Use the queries in `sql-codes.sql` to analyze the data.

## Architecture diagram

See `ARCHITECTURE.md` for the full ELT architecture diagram.

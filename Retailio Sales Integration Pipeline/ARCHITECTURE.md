# ELT Architecture Diagram

This diagram illustrates the cloud-native ELT pipeline implemented in this internship project.

flowchart TB
    subgraph "Local Environment"
        LocalData["dataset/ folder<br/>Raw CSV files"]
        UploadScript["upload_s3.py<br/>Python + Boto3"]
    end

    subgraph "AWS Cloud"
        S3["AWS S3 Bucket<br/>Raw Data Landing Zone"]
    end

    subgraph "Data Integration"
        Airbyte["Airbyte<br/>ETL Tool"]
    end

    subgraph "Analytics Warehouse"
        MotherDuck["MotherDuck<br/>DuckDB-based Analytics"]
    end

    subgraph "Analysis & Reporting"
        SQLQueries["SQL Queries<br/>Data Exploration"]
        Reports["Reports & Insights"]
    end

    LocalData --> UploadScript
    UploadScript --> S3
    S3 --> Airbyte
    Airbyte --> MotherDuck
    MotherDuck --> SQLQueries
    SQLQueries --> Reports

    style LocalData fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style UploadScript fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    style S3 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Airbyte fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    style MotherDuck fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    style SQLQueries fill:#f9fbe7,stroke:#827717,stroke-width:2px
    style Reports fill:#e0f2f1,stroke:#004d40,stroke-width:2px

## Pipeline Flow Explanation

1. **Data Preparation**: Raw CSV datasets are stored in the local `dataset/` folder.
2. **Upload to Cloud**: The `upload_s3.py` script uses Python and Boto3 to upload files to an AWS S3 bucket.
3. **Data Ingestion**: Airbyte connects to the S3 bucket as a source and extracts the raw data.
4. **Data Loading**: Airbyte transforms and loads the data into MotherDuck, a serverless analytics warehouse.
5. **Data Analysis**: SQL queries are executed in MotherDuck to explore, validate, and analyze the data.
6. **Reporting**: Insights and reports are generated from the analyzed data.

## Key Components

- **AWS S3**: Serves as the raw data landing zone, providing scalable object storage.
- **Airbyte**: Open-source data integration platform handling ETL operations.
- **MotherDuck**: Cloud-native analytics database based on DuckDB for fast querying.
- **Python & Boto3**: Scripting language and AWS SDK for automated uploads.
- **SQL**: Query language for data analysis and reporting.

This architecture demonstrates a modern, cloud-native approach to data engineering, emphasizing scalability, automation, and ease of use.
# Architecture Diagram

This repository implements a simple cloud-native ELT pipeline using AWS S3, Airbyte, MotherDuck, Python, and Boto3.

```mermaid
flowchart TB
    LocalData["Local dataset/ folder"] -->|Upload via Python + Boto3| S3[AWS S3 (raw data storage)]
    S3 -->|Airbyte S3 source connector| Airbyte[Airbyte]
    Airbyte -->|Destination connector| MotherDuck[MotherDuck analytics warehouse]
    MotherDuck -->|SQL queries| Analysis["Query and analyze data"]

    style LocalData fill:#f9f,stroke:#333,stroke-width:1px
    style S3 fill:#0b6fab,stroke:#333,stroke-width:1px,color:#fff
    style Airbyte fill:#fa8c16,stroke:#333,stroke-width:1px,color:#fff
    style MotherDuck fill:#2d8cf0,stroke:#333,stroke-width:1px,color:#fff
    style Analysis fill:#50a14f,stroke:#333,stroke-width:1px,color:#fff
```

## Pipeline summary

- Raw CSV files begin in the local `dataset/` directory.
- `upload_s3.py` uploads those files to an S3 bucket using `boto3`.
- Airbyte connects to the S3 bucket as a source.
- Airbyte syncs the raw data into MotherDuck.
- MotherDuck stores the ingested data and makes it available for SQL queries.

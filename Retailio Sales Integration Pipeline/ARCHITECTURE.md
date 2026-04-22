# Retailio Sales Integration Pipeline - Architecture

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         RETAILIO DATA INTEGRATION PLATFORM                      │
└─────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   SOURCE     │     │   STORAGE    │     │   INGESTION  │     │   WAREHOUSE  │
    │   LAYER      │     │   LAYER      │     │   LAYER      │     │   LAYER      │
    └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
           │                    │                    │                    │
           ▼                    ▼                    ▼                    ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐      ┌──────────────┐
    │   Local CSV  │────▶│   AWS S3     │────▶│   Airbyte    │────▶│  MotherDuck │
    │   Files      │     │   (Data Lake)│     │   (ELT)      │      │  (Warehouse) │
    │              │     │              │     │              │      │              │
    └──────────────┘     └──────────────┘     └──────────────┘      └──────────────┘
           │                                                              │
           │                      ┌──────────────┐                        │
           │                      │   ANALYTICS  │                        │
           │                      │    LAYER     │                        │
           │                      └──────────────┘                        │
           │                            │                                 │
           ▼                            ▼                                 │
    ┌──────────────┐              ┌──────────────┐                        │
    │ upload_s3.py │              │  SQL Queries │                        │
    │ (Boto3)      │              │  & Reports   │                        │
    └──────────────┘              └──────────────┘                        │
```

---

## Architecture Layers

### 1. Source Layer

| Component | Description |
|-----------|-------------|
| **Local CSV Files** | Raw datasets in `dataset/` folder (Sales, Customers, Products) |
| **Data Formats** | CSV and JSON for structured data processing |
| **Data Sources** | Multiple regional branches and online platforms |

### 2. Storage Layer (AWS S3)

| Component | Description |
|-----------|-------------|
| **S3 Bucket** | Centralized data lake for raw and structured data |
| **Folder Structure** | Organized by data type (Sales, Customers, Products) |
| **Purpose** | Scalable object storage serving as landing zone |

### 3. Ingestion Layer (Airbyte)

| Component | Technology | Purpose |
|-----------|------------|---------|
| **ELT Tool** | Airbyte | Extract, load, and sync data from S3 to MotherDuck |
| **Source Connector** | AWS S3 | Reads data from S3 bucket |
| **Destination Connector** | MotherDuck | Loads data into analytics warehouse |
| **Sync Mode** | Full refresh / Incremental |

### 4. Warehouse Layer (MotherDuck)

| Component | Description |
|-----------|-------------|
| **Database** | Serverless cloud warehouse based on DuckDB |
| **Schema** | `retail_data` schema for all ingested tables |
| **Query Engine** | Fast SQL querying for analytics |

### 5. Analytics Layer

| Component | Description |
|-----------|-------------|
| **SQL Queries** | Data exploration and validation |
| **Reports** | Sales summaries, customer insights, top products |
| **Business Intelligence** | Marketing, operations, and finance insights |

---

## Data Flow

### Step 1: Data Preparation
```
Local dataset/ folder → CSV files (Sales, Customers, Products)
```
- Raw data files stored in local `dataset/` folder
- Files include: `sales_V2.csv`, `customer_V2.csv`, `product_V2.csv`

### Step 2: Cloud Upload
```
Local Files → upload_s3.py (Python + Boto3) → AWS S3
```
- Python script uses Boto3 SDK to upload files to S3
- Automated process replaces manual uploads

### Step 3: Data Ingestion
```
AWS S3 → Airbyte Connector → MotherDuck
```
- Airbyte connects to S3 as source
- Extracts raw data and loads into MotherDuck
- Handles schema mapping and data type conversion

### Step 4: Data Analysis
```
MotherDuck → SQL Queries → Business Insights
```
- Run analytical queries for:
  - Sales summary
  - Customer insights
  - Top products analysis

---

## Dataset Schema

### Sales Data

| Column | Type | Description |
|--------|------|-------------|
| sale_id | STRING | Unique transaction identifier |
| product_id | STRING | Product reference |
| customer_id | STRING | Customer reference |
| sale_date | DATE | Date of transaction |
| quantity | INTEGER | Number of items sold |
| unit_price | NUMBER | Price per unit |
| total_amount | NUMBER | Total transaction value |

### Customer Data

| Column | Type | Description |
|--------|------|-------------|
| customer_id | STRING | Unique customer identifier |
| customer_name | STRING | Customer full name |
| email | STRING | Customer email address |
| phone | STRING | Contact number |
| address | STRING | Physical address |
| city | STRING | City location |
| state | STRING | State/Region |
| zip_code | STRING | Postal code |
| registration_date | DATE | Account creation date |

### Product Data

| Column | Type | Description |
|--------|------|-------------|
| product_id | STRING | Unique product identifier |
| product_name | STRING | Product name |
| category | STRING | Product category |
| brand | STRING | Brand name |
| unit_price | NUMBER | Standard price |
| stock_quantity | INTEGER | Available inventory |
| supplier | STRING | Supplier information |

---

## Project Structure

```
Retailio Sales Integration Pipeline/
├── README.md                    # Project overview
├── ARCHITECTURE.md              # This file
├── upload_s3.py                 # Python script for S3 upload
├── sql_code.sql                 # SQL queries for analysis
├── dashboard.ipynb              # Jupyter notebook for visualization
├── dataset/
│   ├── sales_V2.csv             # Sales transaction data
│   ├── customer_V2.csv          # Customer information
│   └── product_V2.csv           # Product catalog
└── Images/                      # Architecture diagrams
```

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Cloud Storage** | AWS S3 | Centralized data lake |
| **ELT Tool** | Airbyte | Data integration and sync |
| **Data Warehouse** | MotherDuck | Serverless analytics warehouse |
| **Scripting** | Python + Boto3 | Automated uploads |
| **Query Engine** | SQL | Data analysis |
| **Orchestration** | Airflow / Cron | Scheduling (optional) |

---

## Project Scope

### Week 1 – Data Lake & Integration Setup

**Goal**: Establish foundational architecture and automate initial data ingestion.

**Deliverables**:
- Create S3 bucket and organize folders for raw data (Sales, Customers, Products)
- Configure Airbyte with S3 as source and MotherDuck as destination
- Test first ingestion run to ensure data mapping and schema alignment
- Verify access permissions, connectivity, and logging setup

**Milestone**: Data successfully moves from S3 → Airbyte → MotherDuck

### Week 2 – Validation & Analytics Enablement

**Goal**: Validate pipeline integrity and prepare data for analysis.

**Deliverables**:
- Create schema `retail_data` in MotherDuck for all ingested tables
- Validate record counts, schema consistency, and null values
- Run analytical SQL queries for insights (sales_summary, customer_insights, top_products)
- Document entire workflow and pipeline architecture

**Milestone**: End-to-end data pipeline functional and validated for analytics readiness

---

## Data Quality & Validation

### Validation Checks

| Check | Description |
|-------|-------------|
| **Record Count** | Verify row counts match between source and destination |
| **Schema Consistency** | Ensure column names and types align |
| **Null Values** | Check for missing or null values in required fields |
| **Data Type** | Validate numeric, date, and string formats |

### SQL Validation Queries

```sql
-- Record count validation
SELECT COUNT(*) FROM sales;
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM products;

-- Null value check
SELECT * FROM sales WHERE sale_id IS NULL;

-- Data consistency
SELECT COUNT(DISTINCT customer_id) FROM sales;
```

---

## Security & Access

### S3 Configuration
- Bucket policies for access control
- IAM roles for Airbyte integration
- Encryption at rest (SSE-S3)

### MotherDuck Access
- Service account for Airbyte connection
- Query permissions for analytics users

---

## Expected Outcomes

- **Fully functional data integration pipeline** connecting AWS S3, Airbyte, and MotherDuck
- **Clean, validated data** available in the warehouse for analytics
- **Centralized and version-controlled datasets** for consistent reporting
- **Reduced manual workload** and improved data reliability
- **Scalable foundation** to support future data modeling, dashboards, and advanced analytics

---

## Future Enhancements

| Enhancement | Description |
|-------------|-------------|
| **Incremental Sync** | Replace full refresh with CDC for faster loads |
| **Data Modeling** | Add dbt transformations for star schema |
| **BI Dashboards** | Integrate with Looker/Tableau for visualization |
| **Real-time Analytics** | Add streaming pipeline for near real-time insights |
| **Additional Sources** | Expand to include more data sources |

---

## Conclusion

This architecture provides Retailio with:

1. **Centralized Data Platform** - Single source of truth for sales, customer, and product data
2. **Automated Pipeline** - Reduced manual effort through Airbyte integration
3. **Scalable Storage** - AWS S3 handles growing data volumes
4. **Fast Analytics** - MotherDuck provides instant SQL query performance
5. **Business Ready** - Data validated and ready for reporting

The architecture follows modern ELT best practices, enabling Retailio to make data-driven decisions faster and more reliably.
# AcmeMart Transaction Analytics - Architecture

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              ACEMART DATA PLATFORM                              │
└─────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   SOURCE     │     │   INGESTION  │     │   STORAGE    │     │  TRANSFORM  │
    │   SYSTEMS    │     │    LAYER     │     │    LAYER     │     │    LAYER     │
    └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
           │                    │                    │                    │
           ▼                    ▼                    ▼                    ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Google     │────▶│   Airbyte    │────▶│   Snowflake  │────▶│     dbt      │
    │   Drive      │     │   (Bronze)   │     │   (Warehouse)│     │   (Gold)     │
    │   (CSV)      │     │              │     │              │     │              │
    └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                              │
                                                                              ▼
                                                                   ┌──────────────┐
                                                                   │   ANALYTICS  │
                                                                   │    LAYER     │
                                                                   └──────────────┘
                                                                        │
                                                                        ▼
                                                                 ┌──────────────┐
                                                                 │  Business    │
                                                                 │  Users       │
                                                                 └──────────────┘
```

---

## Architecture Layers

### 1. Source Layer

| Component | Description |
|-----------|-------------|
| **Google Drive** | Contains raw CSV transaction files from multiple store sources |
| **Data Files** | CSV files with transaction data (transaction_id, amount, date, status) |
| **Format** | Semi-structured CSV with inconsistent data types |

### 2. Ingestion Layer

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Airbyte** | ELT Tool | Extract and load data from Google Drive to Snowflake |
| **Bronze Schema** | Snowflake | Raw data landing zone - stores unprocessed data |
| **Connector** | Google Drive Source | Reads CSV files and imports to warehouse |

### 3. Storage Layer (Snowflake)

| Schema | Purpose | Tables |
|--------|---------|--------|
| **Bronze** | Raw ingestion layer | Raw transaction data |
| **Silver (Staging)** | Cleansed and standardized | `stg_transactions` |
| **Gold** | Business-ready analytics | `fct_transactions` |

### 4. Transformation Layer

| Component | Technology | Purpose |
|-----------|------------|---------|
| **dbt** | SQL-based transformation | Data modeling, cleaning, and aggregation |
| **Staging Models** | SQL views/tables | Standardize column names and data types |
| **Fact Models** | SQL tables | Business-level aggregations |
| **Tests** | dbt tests | Data quality validation |

### 5. Analytics Layer

| Component | Description |
|-----------|-------------|
| **SQL Queries** | Business intelligence queries |
| **Reports** | Revenue, transaction trends, category analysis |
| **Self-Service** | Business users can query directly |

---

## Data Flow

### Step 1: Data Extraction
```
Google Drive (CSV) → Airbyte Connector → Snowflake Bronze Schema
```
- Airbyte reads CSV files from Google Drive
- Data is loaded into Bronze schema without transformation
- Maintains raw data integrity for audit purposes

### Step 2: Staging (Silver Layer)
```
Bronze Schema → dbt stg_transactions → Staging Layer
```
- dbt reads raw data from Bronze
- Applies data type conversions
- Standardizes column names
- Validates data quality

### Step 3: Gold Layer (Fact Table)
```
Staging Layer → dbt fct_transactions → Gold Layer
```
- Creates surrogate keys
- Adds derived columns (transaction_category)
- Aggregates data for analytics

### Step 4: Analytics & Reporting
```
Gold Layer → SQL Queries → Business Insights
```
- Business users run queries
- Generate reports on revenue, trends, categories

---

## Data Models

### Staging Model (stg_transactions)

```
┌─────────────────────┬─────────────┬────────────────────────────────────────────┐
│     Column          │    Type     │              Description                   │
├─────────────────────┼─────────────┼────────────────────────────────────────────┤
│ transaction_id      │ STRING      │ Unique identifier for each transaction     │
│ amount              │ NUMBER      │ Transaction amount                         │
│ transaction_date    │ DATE        │ Date of transaction                        │
│ status              │ STRING      │ Transaction status                         │
└─────────────────────┴─────────────┴────────────────────────────────────────────┘
```

**Transformations:**
- Data type standardization
- Null handling
- Basic validation

### Fact Model (fct_transactions)

```
┌─────────────────────┬─────────────┬────────────────────────────────────────────┐
│     Column          │    Type     │              Description                   │
├─────────────────────┼─────────────┼────────────────────────────────────────────┤
│ transaction_key     │ INTEGER     │ Surrogate key (auto-increment)             │
│ transaction_id      │ STRING      │ Original transaction identifier            │
│ amount              │ NUMBER      │ Transaction amount                         │
│ transaction_date    │ DATE        │ Date of transaction                        │
│ transaction_category│ STRING      │ 'High Value' if amount > 1000, else       │
│                     │             │ 'Standard'                                 │
└─────────────────────┴─────────────┴────────────────────────────────────────────┘
```

**Business Logic:**
- Categorizes transactions based on amount threshold
- Creates surrogate key for join optimization

---

## Data Quality & Testing

### dbt Tests Implemented

| Test | Model | Column | Purpose |
|------|-------|--------|---------|
| `unique` | stg_transactions | transaction_id | Ensures no duplicate transactions |
| `not_null` | stg_transactions | transaction_id | Ensures all records have ID |
| `accepted_values` | stg_transactions | amount | Validates amount is positive |

### Data Quality Checks

- **Uniqueness**: No duplicate transaction IDs
- **Completeness**: All required fields populated
- **Validity**: Amount values within expected range
- **Consistency**: Date formats standardized

---

## Infrastructure Components

### Snowflake Configuration

| Component | Configuration |
|-----------|---------------|
| **Warehouse** | Compute cluster for data processing |
| **Database** | ACEMART_DB |
| **Schemas** | BRONZE, SILVER, GOLD |
| **Storage** | Cloud storage (AWS S3 / Azure Blob) |

### Airbyte Configuration

| Component | Configuration |
|-----------|---------------|
| **Source** | Google Drive |
| **Destination** | Snowflake |
| **Sync Mode** | Full refresh |
| **Schedule** | Daily batch |

### dbt Configuration

| Component | Configuration |
|-----------|---------------|
| **Profile** | snowflake |
| **Target** | dev/prod |
| **Models** | staging, fact |
| **Tests** | schema + data tests |

---

## Project Structure

```
AcmeMart Transaction Analytics/
├── README.md                    # Project overview
├── ARCHITECTURE.md              # This file
├── dbt_project.yml              # dbt configuration
├── profiles.yml                 # dbt profiles
├── schema_creation.sql          # Database schema setup
├── airbyte_snowflake.sql        # Airbyte destination config
├── airbyte_grant.sql            # Airbyte permissions
├── data_check.sql               # Data validation queries
├── warehouse_verify.sql         # Warehouse verification
├── network_policy.sql           # Network security
├── test.sql                     # Test queries
├── models/
│   ├── sources.yml              # dbt sources configuration
│   ├── schema.yml               # Model schemas
│   ├── stg_transactions.sql     # Staging model
│   └── fct_transactions.sql     # Fact model
└── data sources/
    └── data_2/                  # Source CSV files
        ├── store_*.csv          # Store transaction files
```

---

## Security & Access

### Network Policy
- IP whitelisting for Snowflake access
- VPC configuration for secure connections

### Role-Based Access
- **Airbyte Service Account**: Read access to source, write to Bronze
- **dbt Service Account**: Read Bronze, write to Silver/Gold
- **Business Analysts**: Read Gold layer only

### Data Encryption
- Snowflake encryption at rest
- TLS for data in transit

---

## Scalability Considerations

| Aspect | Current State | Future Enhancement |
|--------|---------------|-------------------|
| **Data Volume** | Single daily batch | Incremental loads |
| **Sources** | Google Drive only | Multiple source connectors |
| **Transformation** | Batch (dbt) | Real-time (Spark/Glue) |
| **Analytics** | SQL queries | BI dashboards (Looker/Tableau) |

---

## Monitoring & Operations

### Pipeline Monitoring
- Airbyte connection status
- dbt run success/failure
- Snowflake query performance

### Operational Metrics
- Data freshness (time since last load)
- Record counts per layer
- Test pass/fail rates

### Troubleshooting
- Airbyte logs for extraction issues
- dbt logs for transformation errors
- Snowflake query history for performance

---

## Conclusion

This architecture provides AcmeMart with:

1. **Centralized Data Platform** - Single source of truth for transaction data
2. **Scalable Foundation** - Ready for future data sources and use cases
3. **Data Quality** - Validated through dbt tests
4. **Self-Service Analytics** - Business users can query directly
5. **Maintainable Code** - Version-controlled with Git

The architecture follows industry best practices with a layered approach (Bronze → Silver → Gold) enabling clean separation of concerns and easy troubleshooting.
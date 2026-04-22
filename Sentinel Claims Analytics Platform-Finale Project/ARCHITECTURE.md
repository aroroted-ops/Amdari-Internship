# Sentinel Claims Analytics Platform - Architecture

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                        SENTINEL CLAIMS ANALYTICS DATA PLATFORM                              │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   SOURCE     │     │   STORAGE    │     │  PROCESSING  │     │   WAREHOUSE  │     │TRANSFORMATION│
    │   LAYER      │     │   LAYER      │     │   LAYER      │     │   LAYER      │     │    LAYER     │
    └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
           │                    │                    │                    │                    │
           ▼                    ▼                    ▼                    ▼                    ▼
    ┌──────────────┐     ┌──────────────┐      ┌──────────────┐      ┌──────────────┐     ┌──────────────┐
    │   CSV Files  │────▶│   AWS S3     │────▶│   AWS Glue   │────▶│    Amazon    │────▶│     dbt      │
    │   (Multiple  │     │   (Data      │      │   (PySpark   │      │   Redshift   │     │ (Transform)  │
    │   Sources)   │     │   Lake)      │      │     ETL)     │      │   (DWH)      │     │              │
    └──────────────┘     └──────────────┘      └──────────────┘      └──────────────┘     └──────────────┘
                                                                              │                    │
                                                                              ▼                    ▼
                                                                   ┌──────────────┐     ┌──────────────┐
                                                                   │   ANALYTICS  │     │   ANALYTICS  │
                                                                   │    LAYER     │     │    LAYER     │
                                                                   └──────────────┘     └──────────────┘
                                                                         │
           ┌─────────────────────────────────────────────────────────────┘
           ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │ORCHESTRATION │     │  MONITORING  │     │INFRASTRUCTURE│
    │   LAYER      │     │   LAYER      │     │    LAYER     │
    └──────────────┘     └──────────────┘     └──────────────┘
           │                    │                    │
           ▼                    ▼                    ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Airflow    │     │ CloudWatch   │     │  Terraform   │
    │   (DAGs)     │     │(Logs/Metrics)│     │   (IaC)      │
    └──────────────┘     └──────────────┘     └──────────────┘
```

---

## Architecture Layers

### 1. Source Layer

| Component | Description |
|-----------|-------------|
| **CSV Data Feeds** | Unstructured/semi-structured data from multiple employers, insurance carriers, and TPAs |
| **Data Formats** | CSV with inconsistent schemas, missing fields, and schema drift |
| **Data Types** | Claims data, policy data, payment records, employer information |

### 2. Storage Layer (AWS S3)

| Zone | Purpose | Storage Format |
|------|---------|----------------|
| **Raw Zone** | Landing zone for ingested CSV files | CSV (original format) |
| **Landing Zone** | Staging area after initial validation | CSV / JSON |
| **Processed Zone** | Cleaned and transformed data | Parquet (optimized) |

### 3. Processing Layer (AWS Glue)

| Component | Description |
|-----------|-------------|
| **PySpark Jobs** | ETL scripts for data cleaning and transformation |
| **Schema Drift Handling** | Dynamic schema inference and validation |
| **Data Validation** | Quality checks and anomaly detection |
| **Format Conversion** | CSV to Parquet transformation |

### 4. Warehouse Layer (Amazon Redshift)

| Schema | Purpose | Content |
|--------|---------|---------|
| **Staging** | Raw imported tables | Raw data from Glue |
| **Dimensions** | Dimension tables | Employer, Claimant, Policy, Date dimensions |
| **Facts** | Fact tables | Claims, Payments, Settlements |
| **Analytics** | Aggregated views | Business metrics and KPIs |

### 5. Transformation Layer (dbt)

| Component | Description |
|-----------|-------------|
| **SQL Transformations** | Business logic and data transformations |
| **Data Modeling** | Star schema with fact and dimension tables |
| **Testing** | Built-in data quality tests and validations |
| **Documentation** | Self-documenting models and lineage |
| **Version Control** | Git-based version control for transformations |

### 6. Analytics Layer

| Component | Description |
|-----------|-------------|
| **SQL Queries** | Ad-hoc analysis and reporting |
| **BI Tools** | Dashboards for business users |
| **Metrics** | Key performance indicators |

---

## Data Lake Architecture

### Multi-Zone Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│                        AWS S3 DATA LAKE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐    ┌─────────────┐     ┌─────────────┐        │
│   │    RAW      │───▶│   LANDING   │───▶│  PROCESSED  │        │
│   │    ZONE     │    │    ZONE     │     │    ZONE     │        │
│   └─────────────┘    └─────────────┘     └─────────────┘        │
│         │                  │                  │                 │
│         ▼                  ▼                  ▼                 │
│   Ingested CSV      Validated data     Cleaned & optimized      │
│   files             (with schema       (Parquet format)         │
│                     tracking)                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Ingestion**: CSV files uploaded to Raw zone (S3)
2. **Validation**: Schema check and basic validation in Landing zone
3. **Transformation**: Clean, standardize, convert to Parquet in Processed zone (Glue)
4. **Loading**: Load to Redshift staging tables
5. **Modeling**: Transform and model data using dbt
6. **Analytics**: Create dimension and fact tables, generate business metrics

---

## Data Modeling

### Dimensional Model

```
┌─────────────────────────────────────────────────────────────────┐
│                      STAR SCHEMA DESIGN                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                    ┌─────────────────┐                          │
│                    │   FACT TABLE    │                          │
│                    │ fct_claims      │                          │
│                    └────────┬────────┘                          │
│                             │                                   │
│         ┌──────────┬────────┼────────┬──────────┐               │
│         │          │        │        │          │               │
│         ▼          ▼        ▼        ▼          ▼               │
│   ┌──────────┐┌──────────┐┌──────────┐┌──────────┐┌──────────┐  │
│   │dim_employ││dim_claim ││dim_policy││dim_date  ││dim_paymnt│  │
│   │   er     ││   ant    ││          ││          ││   ent    │  │
│   └──────────┘└──────────┘└──────────┘└──────────┘└──────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Dimension Tables

| Table | Description | SCD Type |
|-------|-------------|----------|
| **dim_employer** | Employer information and risk profiles | Type 2 |
| **dim_claimant** | Claimant demographics and details | Type 2 |
| **dim_policy** | Policy terms, coverage, and renewals | Type 2 |
| **dim_date** | Calendar dimension for time analysis | N/A |
| **dim_payment** | Payment types and settlement info | Type 2 |

### Fact Tables

| Table | Description | Grain |
|-------|-------------|-------|
| **fct_claims** | Workers' compensation claims | One claim per row |
| **fct_payments** | Claim payment transactions | One payment per row |
| **fct_settlements** | Claim settlement details | One settlement per row |

---

## Slowly Changing Dimensions (SCD Type 2)

### Implementation Strategy

```sql
-- SCD Type 2 tracking for dimension tables
ALTER TABLE dim_employer
ADD COLUMN effective_date DATE,
ADD COLUMN expiration_date DATE,
ADD COLUMN is_current BOOLEAN;
```

### Historical Tracking

| Field | Purpose |
|-------|---------|
| **effective_date** | Start date of the record version |
| **expiration_date** | End date of the record version |
| **is_current** | Flag for current active record |
| **version** | Version number for audit trail |

---

## Orchestration Layer (Apache Airflow)

### DAG Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                     AIRFLOW DAG WORKFLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────┐                                                  │
│   │  Start   │                                                  │
│   └────┬─────┘                                                  │
│        ▼                                                        │
│   ┌──────────┐                                                  │
│   │Ingest S3 │──────┐                                           │
│   └────┬─────┘      │                                           │
│        ▼            │                                           │
│   ┌──────────┐      │      ┌──────────┐                         │
│   │Validate  │──────┼────▶│  Retry   │                          │
│   │  Data    │      │      └────┬─────┘                         │
│   └────┬─────┘      │          │                                │
│        ▼            │          ▼                                │
│   ┌──────────┐      │     ┌──────────┐                          │
│   │Transform │──────┘     │  Alert   │                          │
│   │ (Glue)   │            └────┬─────┘                          │
│   └────┬─────┘                  │                               │
│        ▼                        │                               │
│   ┌──────────┐                  │                               │
│   │Load DWH  │──────────────────┘                               │
│   └────┬─────┘                                                  │
│        ▼                                                        │
│   ┌──────────┐                                                  │
│   │Transform │──────┐                                           │
│   │  (dbt)   │      │                                           │
│   └────┬─────┘      │                                           │
│        ▼            │                                           │
│   ┌──────────┐      │      ┌──────────┐                         │
│   │  Tests   │──────┼────▶│  Alert   │                          │
│   └────┬─────┘      │      └────┬─────┘                         │
│        ▼            │          │                                │
│   ┌──────────┐      │          ▼                                │
│   │  End     │──────┘     ┌──────────┐                          │
│   └──────────┘            │  Retry   │                          │
│                           └────┬─────┘                          │
│                                │                                │
│                                ▼                                │
│                           ┌──────────┐                          │
│                           │  Skip    │                          │
│                           └──────────┘                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Pipeline Features

| Feature | Implementation |
|---------|----------------|
| **Scheduling** | Daily batch jobs with cron expressions |
| **Retries** | Automatic retry on failure (3 attempts) |
| **Dependencies** | Task dependencies for proper flow |
| **Error Handling** | Alert on failure, skip or continue options |
| **Logging** | Full execution logs for debugging |

---

## Monitoring & Observability

### Amazon CloudWatch Integration

| Component | Monitoring |
|-----------|------------|
| **Glue Jobs** | Job execution time, success/failure status |
| **Airflow DAGs** | Task duration, failure alerts |
| **Redshift** | Query performance, storage usage |
| **S3** | Data freshness, bucket metrics |

### Alert Configuration

| Alert Type | Trigger | Action |
|------------|---------|--------|
| **Job Failure** | Glue job fails | Email notification |
| **Data Delay** | No new data > 24h | Alert on-call |
| **Storage Alert** | Redshift storage > 80% | Notify admin |
| **Query Timeout** | Query > 5 minutes | Log for review |

---

## Infrastructure as Code (Terraform)

### Resources Provisioned

| Resource | Purpose |
|----------|---------|
| **S3 Buckets** | Data lake storage (raw, landing, processed) |
| **Glue Jobs** | ETL transformation scripts |
| **Redshift Cluster** | Data warehouse |
| **IAM Roles** | Access control and permissions |
| **VPC** | Network isolation |
| **Security Groups** | Firewall rules |

### Tagging Strategy

| Tag | Example Value | Purpose |
|-----|---------------|---------|
| **Environment** | production, dev | Resource grouping |
| **Project** | sentinel-analytics | Cost allocation |
| **Owner** | data-engineering-team | Responsibility |
| **Cost Center** | analytics | Budget tracking |

---

## Data Quality Framework

### Quality Checks

| Check | Description |
|-------|-------------|
| **Completeness** | No missing required fields |
| **Uniqueness** | No duplicate records |
| **Validity** | Data within expected ranges |
| **Consistency** | Cross-field validation |
| **Timeliness** | Data within expected timeframe |

### Testing Approach

- **Schema Validation**: Verify column names and types
- **Null Checks**: Ensure required fields populated
- **Referential Integrity**: Foreign key validation
- **Business Rules**: Custom validation logic

---

## Security Architecture

### Data Protection

| Layer | Security Measure |
|-------|------------------|
| **Network** | VPC isolation, security groups |
| **Access** | IAM roles with least privilege |
| **Encryption** | SSE-S3 for S3, SSL for Redshift |
| **Audit** | CloudTrail logging |

### Compliance Features

- **Audit Trail**: All data changes logged
- **Data Lineage**: Full traceability from source to report
- **Retention Policies**: Configurable data lifecycle

---

## Project Structure

```
Sentinel Claims Analytics Platform-Finale Project/
├── README.md                    # Project overview
├── ARCHITECTURE.md              # This file
├── infrastructure/
│   ├── terraform/               # IaC configurations
│   └── scripts/                 # Deployment scripts
├── pipelines/
│   ├── airflow/                 # DAG definitions
│   └── glue/                    # ETL job scripts
├── models/
│   ├── dimensions/              # Dimension table definitions
│   └── facts/                   # Fact table definitions
├── monitoring/
│   ├── dashboards/              # CloudWatch dashboards
│   └── alerts/                  # Alert configurations
└── tests/
    ├── data_quality/            # Quality test scripts
    └── unit/                    # Unit tests
```

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Cloud Storage** | Amazon S3 | Data lake with multi-zone architecture |
| **Data Processing** | AWS Glue | PySpark-based batch ETL |
| **Data Warehouse** | Amazon Redshift | Central analytics warehouse |
| **Orchestration** | Apache Airflow | DAG-based pipeline management |
| **Monitoring** | Amazon CloudWatch | Logs, metrics, and alerts |
| **Infrastructure** | Terraform | Infrastructure as Code |
| **Language** | Python/PySpark | ETL scripting |

---

## Project Scope

### Week 1 – Data Platform Foundation

**Goal**: Establish the core data pipeline by ingesting, cleaning, and structuring raw data into an analytics-ready format.

**Deliverables**:
- Structured S3 data lake (raw + processed)
- Cleaned and standardized datasets (Parquet format)
- Redshift staging tables populated
- Initial data models (facts and dimensions)

### Week 2 – Productionization & Reliability

**Goal**: Automate, monitor, and optimize the pipeline for production readiness and business usability.

**Deliverables**:
- Fully automated pipeline (scheduled DAGs)
- Monitoring dashboards and alert configurations
- Validated, analytics-ready datasets
- Optimized and cost-aware data platform
- Documentation and operational runbooks

---

## Expected Outcomes

At the end of this project, Sentinel will have:

1. **Robust Batch Ingestion Pipeline** - Capable of handling messy, real-world CSV data
2. **Data Lake** - Centralized storage with multi-zone architecture
3. **Analytics-Ready Warehouse** - Properly modeled fact and dimension tables
4. **Historical Visibility** - SCD Type 2 implementation for audit tracking
5. **Improved Reliability** - Monitoring and orchestration for pipeline health
6. **Cost Control** - Basic governance and tagging strategies

---

## Future Enhancements

| Enhancement | Description |
|-------------|-------------|
| **Real-time Processing** | Add streaming pipeline for near real-time data |
| **Data Governance** | Implement data catalog and metadata management |
| **Advanced Analytics** | Add ML models for fraud detection |
| **Self-Service BI** | Integrate with BI tools for business users |
| **Data Sharing** | Enable secure data sharing with partners |

---

## Conclusion

This architecture provides Sentinel Claims Analytics with:

1. **Production-Grade Platform** - Built for reliability and scale
2. **Schema Drift Tolerance** - Handles inconsistent CSV sources
3. **Audit-Ready** - Historical tracking through SCD Type 2
4. **Observable Operations** - Full monitoring and alerting
5. **Cost-Effective** - Optimized storage and compute
6. **Maintainable** - Infrastructure as Code and documented processes

The platform addresses all business challenges including data silos, manual reporting, quality issues, and limited visibility, enabling Sentinel to make data-driven decisions with confidence.
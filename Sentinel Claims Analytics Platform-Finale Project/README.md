# Sentinel Claims Analytics Platform

## Overview

Sentinel Claims Analytics is a data-driven insurance technology company specializing in workers' compensation and occupational risk management. The company aggregates claims data from multiple employers, insurance carriers, and third-party administrators to provide insights into workplace incidents, claim trends, and policy performance.

Operating in a highly regulated environment, Sentinel relies on accurate, auditable, and timely data to support underwriting decisions, fraud detection, and regulatory reporting. However, much of its upstream data arrives as unstructured or semi-structured CSV extracts from disparate systems.

---

## Core Services

| Service | Description |
|---------|-------------|
| **Claims Processing & Management** | End-to-end handling of workers' compensation claims, from incident reporting to adjudication and closure. |
| **Policy & Coverage Administration** | Management of insurance policies, coverage terms, renewals, and premium tracking. |
| **Claims Analytics & Reporting** | Analysis of claim trends, approval rates, payout patterns, and operational performance metrics. |
| **Risk Assessment & Fraud Detection** | Identification of high-risk claims and anomalies to reduce fraud and financial exposure. |
| **Employer & Workforce Insights** | Reporting on employer risk profiles, workplace incidents, and claimant demographics. |
| **Regulatory Compliance & Audit Support** | Ensuring data accuracy, traceability, and adherence to industry regulations through audit-ready reporting. |
| **Payment & Settlement Tracking** | Monitoring claim payouts, payment types, and settlement timelines for financial oversight. |

---

## Business Challenge

Sentinel faces significant data engineering challenges due to the nature of its upstream sources:

- **Inconsistent CSV data feeds** from multiple partners, with frequent schema drift and missing fields
- **No reliable historical tracking**, making it difficult to audit claim updates or policy changes over time
- **Fragmented data pipelines**, leading to delays in analytics and reporting
- **Limited visibility into pipeline failures**, increasing operational risk
- **Growing infrastructure costs** due to inefficient data storage and processing patterns

These issues directly impact the company's ability to deliver accurate insights, meet compliance requirements, and scale its analytics platform.

---

## Team Responsibilities and Collaboration Model

### Data Engineering Responsibilities

The Data Engineering team is responsible for building and maintaining the data platform, pipelines, and infrastructure.

**Core Responsibilities:**

1. **Data Ingestion & Storage**
   - Design and implement ingestion pipelines for raw CSV data
   - Manage S3 data lake structure (raw, staging, curated zones)
   - Handle schema drift and ingestion anomalies

2. **Data Transformation & Processing**
   - Develop ETL/ELT pipelines using PySpark / Glue
   - Clean, standardize, and validate incoming data
   - Convert raw data into optimized formats (Parquet)

3. **Data Modeling**
   - Build and maintain data warehouse models in Redshift
   - Implement:
     - Fact tables
     - Dimension tables
     - Slowly Changing Dimensions

4. **Orchestration & Automation**
   - Develop and maintain workflows using Apache Airflow
   - Schedule batch jobs and manage dependencies
   - Ensure pipeline reliability with retries and SLAs

5. **Monitoring & Reliability**
   - Configure logging, metrics, and alerts using Amazon CloudWatch
   - Monitor pipeline health and performance
   - Troubleshoot and resolve failures

6. **Infrastructure & Security**
   - Provision infrastructure using Terraform
   - Implement IAM roles and access control
   - Ensure encryption and secure data access

7. **Cost Optimization**
   - Manage storage and compute costs

### Data Analytics Responsibilities

The Data Analytics team is responsible for deriving insights and ensuring business usability of data.

**Core Responsibilities:**

1. **Business Requirements Definition**
   - Define reporting and analytics needs
   - Identify key metrics and KPIs
   - Provide domain context (workers' compensation insights)

2. **Data Validation & Quality Assurance**
   - Validate outputs from the data pipeline
   - Ensure:
     - Accuracy
     - Completeness
     - Consistency

3. **Data Exploration & Analysis**
   - Query data in Redshift
   - Perform exploratory analysis
   - Identify trends and anomalies

4. **Semantic Layer & Metrics**
   - Define business-friendly metrics:
     - Total claims
     - Average claim amount
     - Claim approval rate
   - Ensure consistent metric definitions across reports

5. **Reporting & Visualization**
   - Build dashboards and reports (e.g., BI tools)
   - Translate data into actionable insights

6. **Feedback Loop to Engineering**
   - Report data issues or inconsistencies
   - Request new fields or transformations
   - Collaborate on improving data models

---

## Rationale for the Project

To enable scalable growth and meet regulatory requirements, Sentinel needs a production-grade batch data platform capable of handling the complexities of real-world data. This project models the design and implementation of such a system, with focus on:

- Building resilience against messy, unreliable data sources
- Ensuring data consistency and standardization
- Preserving historical changes for auditability
- Enabling scalable analytics in a centralized warehouse
- Providing operational visibility and cost control

---

## Project Objectives

The key objectives of this project are to:

1. Develop a schema drift-tolerant ingestion layer for CSV-based data sources
2. Implement a multi-zone data lake architecture (raw, landing, processed)
3. Build clean and standardized datasets using batch transformation jobs
4. Design and implement dimensional models (facts and dimensions) in the warehouse
5. Enable Slowly Changing Dimensions (Type 2) for tracking historical changes
6. Orchestrate pipelines with automated scheduling, retries, and dependency management
7. Establish monitoring and alerting mechanisms for pipeline health
8. Apply basic cost control strategies and tagging for resource management
9. Deliver a fully documented, reproducible system

---

## Technology Stack

The platform is built using a modern cloud-native stack:

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Cloud Storage** | Amazon S3 | Data lake storage with raw, landing, and processed zones |
| **Data Processing** | AWS Glue | PySpark-based batch ETL jobs for cleaning and transformation |
| **Data Warehouse** | Amazon Redshift | Central analytics warehouse with dimensional modeling |
| **Orchestration** | Apache Airflow | DAG-based pipeline orchestration with retries and scheduling |
| **Monitoring & Logging** | Amazon CloudWatch | Logs, metrics, and alerts for pipeline observability |
| **Infrastructure as Code** | Terraform | Reproducible infrastructure provisioning |

---

## Project Scope

### Week 1 – Data Platform Foundation

**Goal:** Establish the core data pipeline by ingesting, cleaning, and structuring raw data into an analytics-ready format.

**Deliverables:**
- Structured S3 data lake (raw + processed)
- Cleaned and standardized datasets (Parquet format)
- Redshift staging tables populated
- Initial data models (facts and dimensions)

### Week 2 – Productionization & Reliability

**Goal:** Automate, monitor, and optimize the pipeline for production readiness and business usability.

**Deliverables:**
- Fully automated pipeline (scheduled DAGs)
- Monitoring dashboards and alert configurations
- Validated, analytics-ready datasets
- Optimized and cost-aware data platform
- Documentation and operational runbooks

---

## Expected Outcome

At the end of this project, Sentinel will have:

- A robust batch ingestion pipeline capable of handling messy, real-world CSV data
- A data lake
- A clean, analytics-ready data warehouse with properly modeled fact and dimension tables
- Historical visibility into key entities through SCD Type 2 implementation
- Improved reliability and transparency through monitoring and orchestration
- Controlled infrastructure costs with basic governance and tagging strategies

The platform will significantly reduce manual data handling, improve data quality, and enable faster, more reliable analytics.

---

## Deliverables

The project will produce the following deliverables:

- End-to-end data pipeline (S3 → Glue → Redshift → data models)
- Airflow DAGs with scheduling, retries, and failure handling
- Terraform configurations for core infrastructure components
- Monitoring setup (CloudWatch logs, metrics, and alerts)
- Data quality checks and validation tests
- Architecture diagram illustrating system design
- Operational documentation and GitHub repository
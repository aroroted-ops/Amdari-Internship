# AcmeMart Transaction Analytics

## Project Overview

To remain competitive and data-driven, AcmeMart needs a centralized and well-structured data platform.

This project is initiated to:

- Establish a single source of truth for business data
- Enable self-service analytics for business users
- Improve data reliability and consistency
- Transition from reactive reporting to proactive decision-making
- Build a scalable data foundation for future use cases

## Business Challenge

- **Data Silos:** Data is stored in a shared location (Google Drive), but remains logically siloed across multiple source files, with no unified schema or integration layer.
- **Limited Analytics Capability:** Difficulty generating insights like total sales by product, store performance, or customer behavior trends.
- **Manual Reporting:** Teams rely on manual processes and spreadsheets, leading to delays and inconsistencies.
- **Poor Data Quality:** Inconsistent data types and formats.
- **Lack of Scalable Data Model:** No structured data warehouse layer to support analytics.

## Project Objectives

1. **Data Integration:** Consolidate data into a centralized warehouse.
2. **Data Transformation:** Implement staging and gold layers.
3. **Data Modeling:** Create fact and dimension tables.
4. **Aggregation Layer:** Build summarized datasets.
5. **Data Quality & Testing:** Ensure accuracy through validations.
6. **Analytics Enablement:** Make data usable for reporting.

## Technology Stack

- Data Warehouse: Snowflake
- Transformation and Modeling Tool: dbt
- Data Ingestion: Airbyte
- Storage: Google Drive
- Version Control: Git / GitHub

## Project Scope

### Week 1 – Data Integration Pipeline Setup

**Goal:**
Establish a reliable batch ingestion pipeline that loads daily transaction files into structured data stored in Snowflake.

**Deliverables:**
- Screenshot of successful source-to-destination integration
- Screenshot of bronze schema in warehouse
- Screenshot of architecture diagram

### Week 2 – Analytics Enablement, Validation & Documentation

**Goal:**
Enable business analytics through SQL queries, ensure data correctness, and deliver full project documentation.

**Deliverables:**
- Screenshot of SQL query result in warehouse
- Screenshot of dbt documentation page showing folder structure and lineage graph
- Link to GitHub repository

## Expected Outcome

- Centralized data warehouse
- Clean fact and dimension tables
- Aggregated datasets for reporting
- Improved data quality
- Faster insights generation
- Reduced manual reporting

## Deliverables

- Data models (staging, fact, dimension, aggregate)
- dbt project with tests
- Documentation (ERD, data dictionary, architecture)

# Amdari Internship

These are the projects done during my 2-month Amdari internship, designed to help you build, manage, and optimize real-world data systems like a professional data engineer.

## Internship Structure

**Environment:** Remote, collaborative, and mentor-guided  
**Meetings:** Twice a week (≈2 hours or more)  
**Mentorship & Interview Prep:** Every Thursday  
**Expected Time Commitment:** Minimum of 1 hour per day  

Your journey is structured to feel like working in a real engineering environment — where collaboration, accountability, and delivery matter. You'll engage in agile-style planning, sprint execution, and code reviews while solving meaningful data challenges.

## Core Learning Pillars

1. **Data Architecture & System Design**  
   Understand data movement and design scalable system architectures.  
   Learn to model and structure data warehouses and data lakes for analytics and reporting.

2. **Data Ingestion & Pipeline Development**  
   Build ETL/ELT pipelines with real-world datasets.  
   Automate workflows to move and transform data efficiently across systems.

3. **Database Management**  
   Work hands-on with SQL and NoSQL databases.  
   Optimize queries, manage schemas, and handle large-scale data storage.

4. **Data Transformation & Processing**  
   Use Python and SQL to clean, validate, and standardize data.  
   Develop scripts that convert raw data into analytics-ready formats.

5. **Data Orchestration & Automation**  
   Learn to schedule and monitor workflows using tools like Airflow or Prefect.  
   Manage dependencies, handle task failures, and implement logging strategies.

6. **Data Security & Governance**  
   Implement secure access control, compliance, and privacy measures.  
   Understand the principles of responsible data handling.

7. **Collaboration & Documentation**  
   Collaborate via GitHub and apply real-world version control practices.  
   Learn how to document code, track changes, and communicate technical findings effectively.

## Tools and Technologies

You'll gain hands-on experience with some of the most in-demand tools in the data engineering ecosystem:

- **Programming & Scripting:** Python
- **Databases:** SQL, PostgreSQL, MySQL, MongoDB, MotherDuckDB
- **Data Pipelines & Orchestration:** Apache Airflow, Prefect, Airbyte
- **Transformation:** Pandas, PySpark
- **Cloud Platforms:** AWS, Google Cloud, Azure
- **Version Control:** Git, GitHub
- **Visualization:** Power BI, Tableau
- **Deployment:** Docker, Virtual Environments

## Project Experience

Over four months, you'll complete 5–6 hands-on projects, each reflecting a real business scenario, such as:

- **Retail Analytics:** Building an ETL pipeline for automated sales data integration.
- **E-Commerce:** Designing a data warehouse for multi-channel reporting.
- **FinTech:** Streaming real-time transaction data for fraud detection.
- **Healthcare:** Architecting a scalable data lake for patient analytics.
- **Logistics:** Developing a performance-optimized reporting database.

Each project deepens your understanding of how data supports organizational intelligence and how engineers make that flow seamless, reliable, and scalable.

## Current Project: Cloud-native ELT Pipeline

This repository contains one of the internship projects: a cloud-native ELT pipeline using AWS S3, Airbyte, MotherDuck, Python, and Boto3.

### Workflow

1. Raw CSV files are stored locally in the `dataset/` folder.
2. `upload_s3.py` uploads those files into an S3 bucket.
3. Airbyte is configured with an S3 source connector.
4. Airbyte loads the data into MotherDuck.
5. Data is queried in MotherDuck for analysis.

### Repository Contents

- `upload_s3.py` - Python script that uploads dataset files from `dataset/` to S3 using `boto3`.
- `dataset/` - Raw CSV dataset files loaded into the pipeline.
- `sql-codes.sql` - SQL queries used to explore the data in MotherDuck.
- `ARCHITECTURE.md` - Architecture diagram and ELT flow summary.
- Screenshots of Airbyte connections and MotherDuck queries.

### Tools Used in This Project

- **AWS S3** as the landing zone for raw dataset files.
- **Airbyte** to connect S3 as a source and MotherDuck as a destination.
- **MotherDuck** to store and query the ingested data.
- **Python** for scripting the upload process.
- **Boto3** for AWS S3 operations.

### Getting Started

1. Ensure AWS credentials are configured locally.
2. Update `upload_s3.py` with your S3 bucket and file name.
3. Run the script: `python upload_s3.py`
4. In Airbyte, create an S3 source connector and a MotherDuck destination connector.
5. Run the Airbyte sync to load data into MotherDuck.
6. Use the queries in `sql-codes.sql` to analyze the data.

See `ARCHITECTURE.md` for the full ELT architecture diagram.
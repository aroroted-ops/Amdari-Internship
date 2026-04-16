-- 1. Select the database where you want the schema to live
USE DATABASE SNOWFLAKE; 

-- 2. Create the bronze schema
CREATE SCHEMA IF NOT EXISTS BRONZE;

-- 3. (Optional) Verify it was created
SHOW SCHEMAS;
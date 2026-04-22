-- 1. Check that the table exists in your BRONZE schema
SHOW TABLES IN SCHEMA AIRBYTE.BRONZE;

-- 2. Verify row count matches your Google Drive file
SELECT COUNT(*) FROM AIRBYTE.BRONZE.YOUR_TABLE_NAME;

-- 3. Check for duplicates (should return 0 if deduping worked)
SELECT transaction_id, COUNT(*)
FROM AIRBYTE.BRONZE.YOUR_TABLE_NAME
GROUP BY transaction_id
HAVING COUNT(*) > 1;
-- This is your Silver Layer model
WITH raw_data AS (
    SELECT * FROM {{ source('google_drive', 'your_table_name') }}
)

SELECT
    CAST(transaction_id AS STRING) AS transaction_id,
    CAST(amount AS FLOAT) AS amount,
    CAST(transaction_date AS DATE) AS transaction_date,
    TRIM(status) AS status
FROM raw_data
WHERE transaction_id IS NOT NULL
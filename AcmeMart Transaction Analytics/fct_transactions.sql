-- This is your Gold Layer Fact table
SELECT
    {{ dbt_utils.generate_surrogate_key(['transaction_id']) }} AS transaction_key,
    transaction_id,
    amount,
    transaction_date,
    CASE 
        WHEN amount > 1000 THEN 'High Value'
        ELSE 'Standard'
    END AS transaction_category
FROM {{ ref('stg_transactions') }}
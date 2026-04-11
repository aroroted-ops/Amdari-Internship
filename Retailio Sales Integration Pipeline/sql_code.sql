-- #New Cell ------>
-- Checking for Data Intergity
SELECT 
    'Sales Integrity' AS profile,
    COUNT(*) FILTER (WHERE order_id IS NULL) AS null_order_ids,
    COUNT(*) FILTER (WHERE product_id IS NULL) AS null_product_ids,
    COUNT(*) FILTER (WHERE sales IS NULL) AS null_sales_values
FROM my_db.main.sales_V2;

SELECT 
    'Product Integrity' AS profile,
    COUNT(*) FILTER (WHERE product_id IS NULL) AS null_product_ids,
    COUNT(*) FILTER (WHERE sku IS NULL) AS null_skus
FROM my_db.main.product_V2;

-- #New Cell ------>
-- Get a 'fingerprint' of your data
SELECT 
    COUNT(*) AS total_rows,
    SUM(sales) AS total_revenue,
    AVG(profit) AS avg_profit,
    MIN(order_date) AS earliest_order,
    MAX(order_date) AS latest_order,
    COUNT(DISTINCT product_id) AS unique_products
FROM my_db.main.sales_V2;

-- #New Cell ------>
-- SQL to fingerprint the Product Catalog
SELECT 
    COUNT(*) AS total_products,
    SUM(stock_quantity) AS total_units_in_stock,
    ROUND(AVG(price), 2) AS average_retail_price,
    ROUND(AVG(product_ratings), 1) AS average_rating,
    MIN(manufacturing_date) AS oldest_product_mfg,
    MAX(manufacturing_date) AS newest_product_mfg,
    COUNT(DISTINCT product_category) AS category_count
FROM my_db.main.product_V2;

-- #New Cell ------>
-- Check for duplicates (Should return 0 rows)
SELECT order_id, COUNT(*)
FROM my_db.main.sales_V2
GROUP BY order_id
HAVING COUNT(*) > 1;

-- Check for missing IDs (Should return 0)
SELECT COUNT(*) AS null_ids
FROM my_db.main.sales_V2
WHERE order_id IS NULL OR row_id IS NULL;

-- #New Cell ------>
-- Check for duplicates (Should return 0 rows)
SELECT product_id, COUNT(*)
FROM my_db.main.product_V2
GROUP BY product_id
HAVING COUNT(price) < 1000;

-- Check for missing IDs (Should return 0)
SELECT COUNT(*) AS null_ids
FROM my_db.main.product_V2
WHERE product_id IS NULL;


-- #New Cell ------>
-- Check for duplicates (Should return 0 rows)
SELECT product_id, COUNT(*)
FROM my_db.main.product_V2
GROUP BY product_id
HAVING COUNT(price) > 1000;

-- Check for missing IDs (Should return 0)
SELECT COUNT(*) AS null_ids
FROM my_db.main.product_V2
WHERE product_id IS NULL;

-- #New Cell ------>

CREATE OR REPLACE NETWORK POLICY airbyte_policy
ALLOWED_IP_LIST = (
 '80.1.247.70',
 '34.106.109.131',
 '34.106.196.165',
 '34.106.60.246',
 '34.106.229.69',
 '34.106.127.139',
 '34.106.218.58',
 '34.106.115.240',
 '34.106.225.141'
);
-- Apply to your user or account
ALTER USER DAROROTE SET NETWORK_POLICY = airbyte_policy;
-- OR apply account-wide:
-- ALTER ACCOUNT SET NETWORK_POLICY = airbyte_policy;
-- TRIM function 
-- remove leading and trailing spaces 
-- SQL TASK: find customers whose firstname contains leading and trailing spaces.
-- we acn check white spaces in two ways 
-- WAY1:
SELECT 
firstname
FROM customers
WHERE firstname!=TRIM(firstname);

-- WAY2:
SELECT
firstname,
LEN(firstname) AS len_name,
LEN(TRIM(firstname)) AS len_trim_name,
LEN(firstname)-LEN(TRIM(firstname)) AS  flag;

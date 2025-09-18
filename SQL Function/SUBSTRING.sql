-- SUBSTRING FUNCTION: 
-- extracts vlaue at from specific position
SELECT
	firstname,
	SUBSTRING(TRIM(firstname),2,LENGTH(firstname)) AS sub_name
FROM customers
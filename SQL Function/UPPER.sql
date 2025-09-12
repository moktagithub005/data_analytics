-- UPPER function
-- convert all the string to thr upper case.

SELECT 
firstname,
country,
CONCAT(firstname,"  ",country) AS country_nmae,
UPPER(firstname) AS low_name
FROM customers
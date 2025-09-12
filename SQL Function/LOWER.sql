-- LOWER function
-- convert all the sting to thr lower case.

SELECT 
firstname,
country,
CONCAT(firstname,"  ",country) AS country_nmae,
LOWER(firstname) AS low_name
FROM customers
-- CONCAT combine multiple  string ointo one values
-- SQL TASK: conacte first name and country into one column
SELECT 
firstname,
country,
CONCAT(firstname, " - ",country) AS firstname_country
FROM customers

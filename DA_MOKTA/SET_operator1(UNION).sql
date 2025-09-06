-- SET operator simple UNION

SELECT
firstname,
lastname
FROM salesdb.customers

UNION

SELECT 
employee_firstname,
employee_lastname
FROM salesdb.employees
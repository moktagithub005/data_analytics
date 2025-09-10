-- 	INTERSECT operator
-- SQL TASK: find the employees who are customer also

SELECT 
    employee_firstname AS firstname,
    employee_lastname AS lastname
FROM salesdb.employees
INTERSECT
SELECT
    firstname,
    lastname
FROM salesdb.customers;

-- EXCEPT operator 
-- find the employees who are mot cutomers at the same time

SELECT 
    employee_firstname AS firstname,
    employee_lastname AS lastname
FROM salesdb.employees
EXCEPT
SELECT
    firstname,
    lastname
FROM salesdb.customers;

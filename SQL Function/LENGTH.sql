-- strinf function--> LENGTH
-- counts how many character in the string 
SELECT
  firstname,
  LENGTH(firstname) AS len_name
FROM customers;

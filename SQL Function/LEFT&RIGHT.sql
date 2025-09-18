-- LEFT AND RIGHT FUNCTION
-- LEFT FUNCTION: extracts specific number of characters from the start
-- RIGHT FUNCTION:extracts specific number of characters from the end 

SELECT 
	firstname,
	LEFT(firstname,2) AS first_2_char,
    RIGHT(firstname,2) AS last_2_char
    
FROM customers
-- REPLACE function
-- replaces specific character with a new character 
-- SQL TASK: remove dashes(-) from a phone number
SELECT 
'123-456-789' AS phone,
REPLACE('123-456-789','-','') AS clean_phopne
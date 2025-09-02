--  INSERT using  SELECT 
-- move data from source to target table 

-- copy data from "customers" table  into "persons" table 
 INSERT INTO persons(id,persons_name,birth_date,phone)

SELECT 
id,
first_name,
NULL,
'UNKNOWN'
FROM customers

-- we need to look both table structure and write query accordingly 
-- as we copying data from customers table and, table does not contain any phone column so kept it unknown and for NULL we have to check constarint if that column allow null or not 
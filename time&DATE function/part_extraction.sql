-- firstly we will look how can be extract the part from a date like "year", "month" and "day"
-- DAY : --> RETURN THE DAY FROM ADATE
-- MONTH : --> RETURN MONTH FROM A DATE 
-- YEAR : --> RETURN A YEAR FROM A DATE 

SELECT 
orderid,
creationtime,
YEAR(creationtime) AS year,
MONTH(creationtime) AS month,
DAY(creationtime) AS day
FROM salesdb.orders
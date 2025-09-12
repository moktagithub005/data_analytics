-- UNION USE CASES 
-- Combine  information
-- combine similar information before analyzing the data
-- SQL TASK : orders are stored i sepparte tables(Orders and OrdersArchive) combine all orders into one report witout duplicates

SELECT *
FROM salesdb.orders
UNION
SELECT *
FROM salesdb.orders_archive;
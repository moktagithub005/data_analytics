-- how many orders placed in each year 
SELECT 
    YEAR(orderdate) AS OrderYear,
    COUNT(*) AS NrOfOrders
FROM salesdb.orders
GROUP BY YEAR(orderdate);

-- how many orders wrre placed in month 
SELECT
	MONTH(orderdate) AS OrderMonth,
	COUNT(*) AS NrOfOrders
FROM salesdb.orders
GROUP BY MONTH(orderdate);

-- write months in string format rather that number 
SELECT 
MONTHNAME(orderdate) As OrderMonth,
COUNT(*) AS NrOfOrdrs
FROM salesdb.orders
GROUP BY MONTHNAME(orderdate);

-- part Extraction use case data filtering 

SELECT * 
FROM salesdb.orders
WHERE MONTH(orderdate)=2;

-- join multiple tables 
SELECT
	o.orderid,
	o.sales,
	c.firstname AS customer_firstname,
	c.lastname AS customer_lastname,
	p.product_name,
	p.price,
	e.employee_firstname,
	e.employee_lastname
FROM salesdb.orders AS o
LEFT JOIN salesdb.customers AS c
ON o.customerid=c.customerid
LEFT JOIN salesdb.products AS p
ON o.productid=p.productid
LEFT JOIN salesdb.employees AS e
ON o.salespersonid=e.employeeid

    

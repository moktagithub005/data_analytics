-- date format: reset the part of date 
SELECT
  orderid,
  creationtime,
  DATE_FORMAT(creationtime, '%Y-%m-%d %H:%i:00') AS trunc_to_minute
FROM salesdb.orders;

SELECT
  orderid,
  creationtime,
  DATE_FORMAT(creationtime, '%Y-%m-%d %H:00:00') AS trunc_to_hour
FROM salesdb.orders;

SELECT
  orderid,
  creationtime,
  DATE(creationtime) AS trunc_to_day
FROM salesdb.orders;

SELECT
  orderid,
  creationtime,
  DATE_FORMAT(creationtime, '%Y-%m-01') AS trunc_to_month
FROM salesdb.orders;

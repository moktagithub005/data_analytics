USE salesdb;
-- LAST_DAY function will edit all the month to last date of months

SELECT
  orderid,
  creationtime,
  LAST_DAY(creationtime) AS end_of_month
FROM salesdb.orders;

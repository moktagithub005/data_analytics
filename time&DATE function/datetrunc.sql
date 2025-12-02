SELECT
  orderid,
  creationtime,
  DATETRUNC(creationtime, '%s') AS part_second
FROM salesdb.orders;

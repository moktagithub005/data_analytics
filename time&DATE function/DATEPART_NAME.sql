SELECT 
  orderid,
  creationtime,

  -- Returns the full name of the month (e.g., 'September')
  MONTHNAME(creationtime)   AS month_name,

  -- Returns the full name of the weekday (e.g., 'Friday')
  DAYNAME(creationtime)     AS weekday_name,

  -- Returns the year as a number (e.g., 2025)
  YEAR(creationtime)        AS year_number,

  -- Returns the quarter of the year (1–4)
  QUARTER(creationtime)     AS quarter_number,

  -- Returns the week number of the year (default: Sunday as first day, 0–53)
  WEEK(creationtime)        AS week_number,

  -- Returns the day of the year (1–366)
  DAYOFYEAR(creationtime)   AS day_of_year,

  -- Returns the day of the month (1–31)
  DAY(creationtime)         AS day_of_month,

  -- Returns the day of the week (1 = Sunday, 7 = Saturday)
  DAYOFWEEK(creationtime)   AS weekday_number

FROM salesdb.orders;

-- in mysql DATEPART NOT EXIST  RATHER THAN YOU USE QUERY AS BELOW..

SELECT
    -- Extracts the year from the given datetime
    YEAR('2025-09-19 14:35:00')     AS part_year,
    
    -- Returns the week number of the year (default: week starts on Sunday, 1–53)
    WEEK('2025-09-19 14:35:00')     AS part_week,
    
    -- Returns the quarter of the year (1 = Jan–Mar, 2 = Apr–Jun, 3 = Jul–Sep, 4 = Oct–Dec)
    QUARTER('2025-09-19 14:35:00')  AS part_quarter,
    
    -- Extracts the month number (1 = January, 12 = December)
    MONTH('2025-09-19 14:35:00')    AS part_month,
    
    -- Extracts the day of the month (1–31)
    DAY('2025-09-19 14:35:00')      AS part_day,
    
    -- Extracts the hour from the time part (0–23)
    HOUR('2025-09-19 14:35:00')     AS part_hour,
    
    -- Extracts the minute from the time part (0–59)
    MINUTE('2025-09-19 14:35:00')   AS part_minute,
    
    -- Extracts the seconds from the time part (0–59)
    SECOND('2025-09-19 14:35:00')   AS part_second;



-- numeric function: 
-- ROUND: roud off the digits as we do in the math 
-- ABS(ABSOLUTE): return the positive value or absolutr values

SELECT
3.516,
ROUND(3.516,2) AS round_2,
ROUND(3.516,1) AS round_1,
ROUND(3.516,0) AS round_0;

SELECT
-10,
ABS(-10);
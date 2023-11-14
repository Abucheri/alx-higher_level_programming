-- Import the table dump into the hbtn_0c_0 database
-- Display the max temperature of each state ordered by state name
-- USE hbtn_0c_0;
-- source temperatures.sql;
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

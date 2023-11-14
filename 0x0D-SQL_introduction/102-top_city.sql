-- Import the table dump into the hbtn_0c_0 database
-- Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
-- USE hbtn_0c_0;
-- source temperatures.sql;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

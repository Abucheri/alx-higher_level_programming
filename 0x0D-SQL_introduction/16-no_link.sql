-- Script to list all records of the table second_table with a non-empty name value
-- List the score and the name for records with a non-empty name (sorted by descending score)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

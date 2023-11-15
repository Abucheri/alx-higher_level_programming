-- This script lists all the cities of California in the specified MySQL database.
SELECT cities.id, cities.name
  FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
  ORDER BY cities.id ASC;

-- This script lists all cities in the specified MySQL database along with their states.
SELECT cities.id, cities.name, states.name
  FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

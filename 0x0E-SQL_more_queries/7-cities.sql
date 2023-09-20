-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Find the state ID for California
SELECT id
FROM states
WHERE name = 'California';

-- List all cities in California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;

-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Find the state ID for California
SELECT @california_state_id := id
FROM states
WHERE name = 'California';
-- List all cities in California
SELECT id, name
FROM cities
WHERE state_id = @california_state_id
ORDER BY id ASC;

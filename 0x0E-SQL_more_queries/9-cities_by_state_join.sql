-- A script that lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states as s
    ON c.state_id = s.id
OrDER BY c.id ASC;
-- a script that creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

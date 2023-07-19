-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the usa database
USE hbtn_0d_usa;

-- create the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL REFERENCES states(id),
	name VARCHAR(256) NOT NULL,
);

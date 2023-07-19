-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

-- creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
        id INT AUTO_INCREMENT UNIQUE NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
);

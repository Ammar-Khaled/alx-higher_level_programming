-- a script that creates the database hbtn_0d_2 and the user user_0d_2.

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- set password for the user
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';

-- grant the select privilege to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

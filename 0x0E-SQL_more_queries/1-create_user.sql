-- a script that creates the MySQL server user user_0d_1 with all privileges.

-- create the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- grant privileges to the user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; 


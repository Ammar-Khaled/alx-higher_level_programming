-- Script that converts hbtn_0c_0 database to UTF8
-- Query to convert hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- by using the `hbtn_0c_0` database
USE hbtn_0c_0;
-- convert the `first` table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

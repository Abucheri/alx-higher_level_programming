-- This script creates the database hbtn_0d_usa and the table states on the specified MySQL server.
-- Create database hbtn_0d_usa if not exists
-- Switch to the hbtn_0d_usa database
-- Check if the table states already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);

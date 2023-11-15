-- This script creates the database hbtn_0d_usa and the table cities on the specified MySQL server.
-- Create database hbtn_0d_usa if not exists
-- Switch to the hbtn_0d_usa database
-- Check if the table cities already exists and create
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);

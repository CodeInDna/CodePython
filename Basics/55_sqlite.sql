-- We are using SQLITE for database

-- Basic SQLITE SYNTAX

-- Datatypes
-- 	NULL	: stores NULL values
-- 	INTEGER : stores integer values
-- 	REAL : stores floating point values
-- 	TEXT : stores text or strings
-- 	BLOB : stores blob of data, stored exactly as it was input
-- 	No Boolean No Date time datatypes

-- In Command Prompt we can use commands:
-- 	.help : gives a description of commands
-- 	It is Connected to a transient in-memory database.


-- Create Table
-- CREATE TABLE cats (
-- 	name TEXT,
-- 	breed TEXT,
-- 	age INTEGER
-- );

-- In cmd we can enter sqlite3 env by using command sqlite3
-- we can open a file using command .open file_name
-- Then, use create command used above
-- check the tables created : .tables


-- INSERT INTO Table
-- INSERT INTO cats(name, breed, age) VALUES('lulu','Scottish Fold', 2);

-- SELECT FROM table
-- SELECT * FROM cats;	# lulu|Scottish Fold|2
INSERT INTO dogs (name, breed, age) VALUES("Champ", "Husky", 4);
INSERT INTO dogs (name, breed, age) VALUES("Rose", "Beagle", 5);
INSERT INTO dogs (name, breed, age) VALUES("Moose", "Lab", 11);
INSERT INTO dogs (name, breed, age) VALUES("Piggy", "Corgi", 2);

-- Read this file:
-- .open dogs_db.db
-- .read 55_sqlite.sql 	(NOTE: cd into directory where this file live)
-- SELECT * FROM dogs;	

-- SELECT * FROM dogs WHERE breed IS "Husky";
-- Champ|Husky|4
-- Champ|Husky|4
-- Champ|Husky|4

-- SELECT * FROM dogs WHERE breed IS NOT "Beagle";
-- Champ|Husky|4
-- Moose|Lab|11
-- Piggy|Corgi|2
-- Champ|Husky|4
-- Moose|Lab|11
-- Piggy|Corgi|2
-- Champ|Husky|4
-- Moose|Lab|11
-- Piggy|Corgi|2

-- SELECT * FROM dogs WHERE breed IS NOT "Beagle" AND breed is NOT "Husky";
-- Moose|Lab|11
-- Piggy|Corgi|2
-- Moose|Lab|11
-- Piggy|Corgi|2
-- Moose|Lab|11
-- Piggy|Corgi|2

-- SELECT * FROM dogs WHERE name LIKE "%gg%";
-- Piggy|Corgi|2
-- Piggy|Corgi|2
-- Piggy|Corgi|2
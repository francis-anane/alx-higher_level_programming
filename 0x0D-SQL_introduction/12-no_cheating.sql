-- This script updates the score of 'Bob' to 10 in the table second_table of a
-- database passed as an argument to mysql command in an MySql server by
-- referencing the name field

UPDATE second_table SET score = 10 WHERE name = 'Bob'

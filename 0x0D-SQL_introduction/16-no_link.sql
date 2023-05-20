-- This script lists all records in the table, second_table of the database
-- hbtn_0c_0 passed as command argument to mysql command in MySQL server
-- except columns where the name value is null
-- The results display the score and name ordered in descending order by the
-- score field of the table

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

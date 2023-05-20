-- This script lists all records with a score >= 10 of the table second_table of
-- the database hbtn_0c_0 passed as argument to mysql command in an MySQL server
-- The results are displayed in descending order ordered by the score

SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC

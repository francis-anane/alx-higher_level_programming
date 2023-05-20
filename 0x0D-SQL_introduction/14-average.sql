-- This script computes the average score of all records
-- in the table second_table of the database hbtn_0c_0 pass as mysql command
-- argument in  MySQL server by aliasing the result as average

SELECT AVG(score) AS average FROM second_table

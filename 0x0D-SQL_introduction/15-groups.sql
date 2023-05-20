-- This script lists the number of records with the same score
-- in the table, second_table table of the hbtn_0c_0 database passed as argument
-- to mysql command in MySQL Server
-- The results are grouped by the score ordered in descending order by the score

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;

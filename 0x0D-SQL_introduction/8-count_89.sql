-- This script dispalys the number of records with id = 89 in the table
-- first_table of the database hbtn_0c_0 passed as
-- a commandline argument to mysql.

SELECT COUNT(id) FROM first_table
WHERE id = 89;

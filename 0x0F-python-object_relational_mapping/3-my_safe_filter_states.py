#!/usr/bin/python3
""" This script lists all value in the states tabel from the database
hbtn_0e_0_usa where state name matches  fourth argument to the script
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    # This query prevents sql injection
    cur.execute("""SELECT * FROM states WHERE name
LIKE %s ORDER BY states.id ASC""", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

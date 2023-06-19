#!/usr/bin/python3
""" This module lists all states from the database
hbtn_0e_0_usa that begins with upper N
The script take 3 arguments which is username, password and the database name
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

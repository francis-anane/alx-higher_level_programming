#!/usr/bin/python3
""" This script lists all cities in the state given as fourth argument
from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id WHERE
states.name=%s""", (argv[4],))
    rows = cur.fetchall()
    row = list(row[0] for row in rows)
    print(*row, sep=", ")
    cur.close()
    conn.close()

#!/usr/bin/python3
"""A  script that lists all states with a name starting with N (upper N)"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY
                '{}' ORDER BY states.id ASC".format(argv[4]")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

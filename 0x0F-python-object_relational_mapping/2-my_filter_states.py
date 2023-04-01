#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """lists all states from the database hbtn_0e_0_usa"""""

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

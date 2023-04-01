#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQL.connect(host="localhost",
                       user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c INNER JOINS
                states AS s ON c.state_id = s.id""")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all cities of that state."""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities\
                 JOIN states\
                 ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC;", (sys.argv[4],))
    states = cur.fetchall()
    print(', '.join(state[0] for state in states))

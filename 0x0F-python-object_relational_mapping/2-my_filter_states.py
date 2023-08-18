#!/usr/bin/python3
"""
This module lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE CONVERT(name USING Latin1)\
                COLLATE Latin1_General_CS\
                = {}\
                ORDER BY id ASC;".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)

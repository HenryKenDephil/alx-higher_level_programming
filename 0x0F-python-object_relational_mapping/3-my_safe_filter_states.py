#!/usr/bin/python3
'''take arguments and display values in the states table
writes a script that is safe from MySQL injections'''
import MySQLdb
import sys
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connector.connect(
        host = "localhost",
        port = 3306,
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name =%s ORDER BY \
        states.id ASC {}".format(argv[4]))
    states = cur.fetchall()
    [print(state) for state in states]
    cur.close()
    db.close()

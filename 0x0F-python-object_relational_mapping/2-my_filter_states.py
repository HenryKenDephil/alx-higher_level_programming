#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
"""
from sys import argv
import MySQLdb
import mysql.connector
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        port=3306,
        host="localhost",
        passwd=sys.argv[2],
        db=sys.rgv[3]
    )
    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    states = my_cursor.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    my_cursor.close()
    db.close()
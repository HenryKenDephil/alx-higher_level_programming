#!/usr/bin/python3
'''script that takes the name of the state\
     as an argument and lists all cities of the state'''

from xmlrpc.client import _HostType
import MySQLdb
import sys

conn = MySQLdb.connector.connect(
    host = "localhost",
    port = "3306",
    User = sys.argv[1],
    passwd=sys.argv[2],
    db = sys.argv[3]
)
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE cities = '%s' ORDER BY\
    cities.id ASC {}".format(sys.argv[4])) 
cities = cur.fetchall()
for city in cities:
    print(city)

conn.close()
cur.close()
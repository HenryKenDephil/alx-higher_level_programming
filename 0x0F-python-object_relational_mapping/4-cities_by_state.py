#!/usr/bin/python3
import mysql.connector
import MySQLdb
import sys

''' script that lists all cities
 from the database hbtn_0e_4_usa'''

 conn = MySQLdb.connector.connect(
    host='localhost', 
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db = argv[3]
 )

 cur = db.cursor()
 cur.execute("SELECT * FROM cities WHERE name = '%s' ORDER BY\
    cities.id ASC{}".format(argv[4]))
cities = cur.fetchall()
[print(city) for cities in cities]
db.close()
cur.close()

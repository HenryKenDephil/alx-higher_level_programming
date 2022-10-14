#!/usr/bin/python3
import MySQLdb
import sys

''' script that lists all cities
 from the database hbtn_0e_4_usa'''

if __name__ == '__main__':
   conn = MySQLdb.connector.connect(
      host='localhost', 
      port=3306,
      user=sys.argv[1],
      passwd=sys.argv[2],
      db = sys.argv[3]
   )

   cur = conn.cursor()
   cur.execute("SELECT * FROM cities WHERE name = '%s' ORDER BY\
      cities.id ASC{}".format(sys.argv[4]))
   cities = cur.fetchall()
   for city in cities:
      print(city)
   
   conn.close()
   cur.close()

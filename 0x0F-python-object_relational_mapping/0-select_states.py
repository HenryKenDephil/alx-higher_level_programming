#!/usr/bin/python3
import sys 
import mysql.connector
import MySQLdb 
#script that lists all states from the db 

if __name__ == '__main__': 
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    my_cursor = db.cursor()   
    my_cursor.execute("SELECT * FROM 'states' ORDER BY states.id")
    [print(states) for states in my_cursor.fetchall()]
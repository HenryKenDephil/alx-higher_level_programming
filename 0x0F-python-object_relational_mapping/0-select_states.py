#!/usr/bin/python3
import sys 
import MySQLdb 
#script that lists all states from the db 

if __name__ == '__main__': 
    db = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user=sys.argv[1], 
        password=sys.argv[2], 
        db=sys.argv[3])
    my_cursor = db.cursor()   
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = my_cursor.fetchall()
    for state in states:
        print(state)
    my_cursor.close()
    db.close()  

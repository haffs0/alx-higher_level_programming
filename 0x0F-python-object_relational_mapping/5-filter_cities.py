#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_0_usa
   by the state name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id ASC""", (sys.argv[4],))
    result = c.fetchall()
    res_len = len(result)
    count = 0
    for row in result:
        if count < res_len - 1:
            print(row[0], end=", ")
            count += 1
        else:
            print(row[0])

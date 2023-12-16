#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = (sys.argv[1], sys.argv[2],
                                                sys.argv[3], sys.argv[4])
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    query = """
    SELECT * FROM cities
    INNER JOIN states
       ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cursor.execute(query)
    print(", ".join([cities[2] for cities in cursor.fetchall()
          if cities[4] == sys.argv[4]]))
    cursor.close()
    db.close()

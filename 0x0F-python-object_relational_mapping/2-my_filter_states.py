#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
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
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

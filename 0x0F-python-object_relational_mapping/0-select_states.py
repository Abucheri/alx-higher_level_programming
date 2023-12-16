#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

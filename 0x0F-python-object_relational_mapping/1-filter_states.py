#!/usr/bin/python3
"""
a script that lists all states with a name starting with N from db using ORM
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            db=database_name
    )

    cursor = db.cursor()
    query = "SELECT *FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

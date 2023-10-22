#!/usr/bin/python3
"""
a python script that lists all states from db using ORM
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
            db=database_name
    )

    cursor = db.cursor()
    query = "SELECT *FROM states ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

#!/usr/bin/python3
"""
a script that lists all values in the states from db using ORM
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()

#!/usr/bin/python3
"""
a script that lists all cities from db using ORM
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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id""")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()

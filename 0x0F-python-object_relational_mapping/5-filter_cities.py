#!/usr/bin/python3
"""
a script that lists cites of that state using the given db
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )

    cursor = db.cursor()
    query = """SELECT cities.name FROM
             cities INNER JOIN states ON states.id=cities.state_id
             WHERE states.name=%s"""
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()

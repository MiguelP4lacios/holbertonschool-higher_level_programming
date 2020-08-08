#!/usr/bin/python3
"""Module 3_my_safe_filter_states
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database,
                         charset="utf8")

    query = db.cursor()

    query.execute(
        "SELECT * FROM states\
        WHERE name = %(searched)s\
        ORDER BY id ASC",
        {'searched': searched})

    for row in query.fetchall():
        print(row)
    query.close()
    db.close()

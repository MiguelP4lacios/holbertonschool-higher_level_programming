#!/usr/bin/python3
"""Module 2_my_filter_states
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
        WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC".format(searched))

    for row in query.fetchall():
        print(row)

    query.close()
    db.close()

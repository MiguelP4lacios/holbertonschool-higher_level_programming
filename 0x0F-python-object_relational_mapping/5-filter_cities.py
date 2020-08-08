#!/usr/bin/python3
"""Module 4_cities_by_states
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database, charset="utf8")

    query = db.cursor()

    query.execute(
        "SELECT cities.name\
        FROM cities\
        INNER JOIN states on cities.state_id = states.id\
        WHERE states.name=%(state)s\
        ORDER BY cities.id ASC;", {'state': state})

    _list = []
    for row in query.fetchall():
        _list.append(row[0])

    print(", ".join(_list))
    query.close()
    db.close()

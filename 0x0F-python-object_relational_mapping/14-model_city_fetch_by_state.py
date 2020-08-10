#!/usr/bin/python3
"""Module 9_model_state_fetch_a
"""
from sys import argv
from model_state import Base as Base_state, State
from model_city import City, Base as Base_city
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connection → mysql+mysqldb://<user>:<passwd>@<host>:<port>/<name_db>'
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    database_url = 'mysql+mysqldb://{}:{}@localhost:3360/{}'.format(
        user, passwd, db)

    engine = create_engine(database_url, pool_pre_ping=True)
    session_basedata = sessionmaker(bind=engine)
    init_basedata = session_basedata()
    query = init_basedata.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for record_s, record_c in query:
        print("{}: ({}) {}".format(record_s.name, record_c.id, record_c.name))
    init_basedata.close()

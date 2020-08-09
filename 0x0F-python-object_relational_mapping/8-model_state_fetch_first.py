#!/usr/bin/python3
"""Module 8_model_state_fetch_first
"""
from sys import argv
from model_state import Base, State
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
    Base.metadata.create_all(engine)
    session_basedata = sessionmaker(bind=engine)
    init_basedata = session_basedata()
    state = init_basedata.query(State).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")

    init_basedata.close()

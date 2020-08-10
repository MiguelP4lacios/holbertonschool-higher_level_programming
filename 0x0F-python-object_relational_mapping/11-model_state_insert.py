#!/usr/bin/python3
"""Module 10_model_state_my_get
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from re import search

if __name__ == "__main__":
    # Connection → mysql+mysqldb://<user>:<passwd>@<host>:<port>/<name_db>'
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    database_url = 'mysql+mysqldb://{}:{}@localhost:3360/{}'.format(
        user, passwd, db)

    engine = create_engine(database_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ed_state = State(name='Louisiana')
    session.add(ed_state)
    session.commit()

    print(ed_state.id)

    session.close()

#!/usr/bin/python3
"""Model city
"""

from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """City class

    Args:
        Base (class): basic class
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=True)
    name = Column(String(128),
                  nullable=True)
    state_id = Column(Integer,
                      ForeignKey(State.id),
                      nullable=True)
    state = relationship(State)

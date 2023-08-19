#!/usr/bin/python3
"""A python file that contains the class definition of a `City`."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Define the City class that links to the MySQL table `cities`."""
    __tablename__ = 'cities'
    id = Column('id', Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('states.id'), nullable=False)

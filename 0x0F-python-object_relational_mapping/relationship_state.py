#!/usr/bin/python3
"""A python file that contains the class definition of a `State`."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """Define the State that links to the MySQL table `states`."""
    __tablename__ = 'states'
    id = Column('id', Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', backref='state')

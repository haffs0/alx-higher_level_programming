#!/usr/bin/python3
"""contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """class definition of a State

    Attributes:
        __tablename__ (str): name of the table
        id:   represents a column of an auto-generated, unique integer,
              can’t be null and is a primary key
        name: represents a column of a string with maximum 128 characters and
              can’t be null
        cities: represent a relationship with the class City

    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

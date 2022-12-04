#!/usr/bin/python3
"""contains the class definition of a Cities and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """class definition of a cities

    Attributes:
        __tablename__ (str): name of the table
        id:   represents a column of an auto-generated, unique integer,
              can’t be null and is a primary key
        name: represents a column of a string with maximum 128 characters and
              can’t be null
        state_id: that represents a column of an integer, can’t be null and
                  is a foreign key to states.id

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

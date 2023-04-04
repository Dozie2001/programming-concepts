#!/usr/bin/python3
"""  a python file that contains the class
   definition of a State and an instance Base = declarative_base():
"""

from sys import argv
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=100)
    name = Column(String(128), nullable=False)

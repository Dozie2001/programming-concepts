#!/usr/bin/python3
"""  a python file that contains the class definition of a State and an instance Base = declarative_base():"""

from sys import argv
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=1 )
    name = Column(String(128), nullable=False)

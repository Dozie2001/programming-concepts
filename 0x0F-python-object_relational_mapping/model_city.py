#!/usr/bin/python3
"""
A module containing a City class
"""
from model_state import Base
from mysqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base



class City(Base):
    """
    A class definition of a City
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey("states.id"))

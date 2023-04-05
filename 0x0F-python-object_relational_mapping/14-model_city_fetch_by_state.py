#!/usr/bin/python3
"""
A script that prints all City objects
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City


if __name_ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session= Session()

    for instance in session.query(State.name, City.id, City.name)
                                  .filter(State.id == City.state_id).order_by(City.id):
        print(f"{instance[0]}: {instance[1]} {instance[2]}")

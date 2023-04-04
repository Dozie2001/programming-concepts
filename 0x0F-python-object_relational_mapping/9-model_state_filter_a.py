#!/usr/bin/python3
""" A  script that lists all State objects that contain the letter a"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(argv[1], argv[2], argv[3]))
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(state.name.like('%a%')):
        print(instance.id, instance.name, sep=': ')

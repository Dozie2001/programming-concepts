#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__=="__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session
    instances = session.query(State).filter(State.name.like('%a%'))

    for instance in instances:
        session.del(instance)
    session.commit()

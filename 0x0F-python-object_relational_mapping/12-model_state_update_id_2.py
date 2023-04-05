#!/usr/bin/python3
"""A script that  changes the name of a State object 
from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id ==  2).first()

    state.name = 'New Mexico'

    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
    
    session.commit()
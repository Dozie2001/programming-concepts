#!/usr/bin/python3
"""A  script that adds the State"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+myslqdb://{}:{}@localhost:{}/{}"
                            .format(argv[1], argv[2], argv[3]))
    
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker()

    session = Session()

    new_state = State(name='Lousiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisana').first()
    print(new_instance.id)

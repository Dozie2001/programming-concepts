#!/usr/bin/python3
"""A script that lists all City objects from the
database"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = creat_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                          .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + instance.name)

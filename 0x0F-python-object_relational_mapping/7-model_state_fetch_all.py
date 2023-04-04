#!/usr/bin/python3
"""A scrit that list all State objects from the database"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for objects in session.query(State).order_by(State.id):
    print(f"{objects.id}: {objects.name}")

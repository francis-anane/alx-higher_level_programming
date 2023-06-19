#!/usr/bin/python3
"""Lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import asc


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(asc(State.id)):
        print(state.id, state.name, sep=": ")
        for city in state.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")

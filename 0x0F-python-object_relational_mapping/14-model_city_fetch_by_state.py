#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Get city by matching foreign key on City with the primary key on State
    for city in (session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id)):
        print(city[0] + ": (" + str(city[1]) + ") " + city[2])

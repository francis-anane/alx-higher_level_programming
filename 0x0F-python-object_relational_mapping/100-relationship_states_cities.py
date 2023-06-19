#!/usr/bin/python3
"""Creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = State(name='California')
    city_name = City(name='San Francisco')
    state_name.cities.append(city_name)

    session.add(state_name)
    session.add(city_name)
    session.commit()

#!/usr/bin/python3
"""This module, defines a class State, and creates
an instance Base, of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """Links to MySQL states table
    Attributes:
        id (int): An auto-generated, unique integer used is as primary key on
the states table
        name (str): Represents a columnn on the table.
        cities (Relationship): Represent a relationship with the class City.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")

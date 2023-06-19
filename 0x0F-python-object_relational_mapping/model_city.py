#!/usr/bin/python3
"""
This module, defines a class City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """Links to MySQL cities table
    Attributes:
        id (int): An auto-generated, unique integer used is as a
    primary key on the cities table
        name (str): Represents a columnn on the table
        state_id (int): Used as a foreign key to states.id on the table states
in a database
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

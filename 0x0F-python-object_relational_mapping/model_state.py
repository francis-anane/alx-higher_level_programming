#!/usr/bin/python3
"""This module, defines a class State, and creates an instance Base,
of declarative_base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """Links to MySQL states table
    Attributes:
        id (int): An auto-generated, unique integer used is as primary key on
the states table
        name (str): Represents a columnn on the table
    """
    __tablename__ = 'states'
    # UNIQUE, NOT NULL, and PRIMARY KEY constrainst set on the id column
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    # NOT NULL, constrainst set on the name column
    name = Column(String(128), nullable=False)

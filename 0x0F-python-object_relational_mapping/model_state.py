#!/usr/bin/python3

"""
Module that defines the State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Class definition for State

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States
        id (int): The unique identifier for a state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

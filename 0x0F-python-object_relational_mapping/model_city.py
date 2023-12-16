#!/usr/bin/python3

"""
Module that defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    Class definition for City.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        id (int): The unique identifier for a city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the states.id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")

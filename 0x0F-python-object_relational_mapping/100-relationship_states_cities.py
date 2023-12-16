#!/usr/bin/python3

"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
"""

from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_state_city(username, password, db_name):
    """
    Creates the State "California" with the City "San Francisco".
    """
    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}"
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name="California", cities=[City(name="San Francisco")])
    session.add(california)
    session.commit()
    session.close()


if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    create_state_city(username, password, db_name)

#!/usr/bin/python3

"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def list_cities_states(username, password, db_name):
    """
    Lists all City objects from the database with their corresponding State.
    """
    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}"
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City).order_by(City.id).all()
    for city in query:
        state_name = city.state.name
        print("{0}: {1} -> {2}".format(city.id, city.name, state_name))
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities_states(username, password, db_name)

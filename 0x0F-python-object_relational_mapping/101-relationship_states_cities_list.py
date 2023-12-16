#!/usr/bin/python3

"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_states_cities(username, password, db_name):
    """
    Lists all State objects and corresponding City objects in the database.
    """
    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}"
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).all()
    for state in query:
        print("{0}: {1}".format(state.id, state.name))
        for city in state.cities:
            print("\t{0}: {1}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    list_states_cities(username, password, db_name)

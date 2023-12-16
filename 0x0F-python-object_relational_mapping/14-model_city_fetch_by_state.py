#!/usr/bin/python3

"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_cities(session):
    """
    Prints all City objects from the database.
    """
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}"
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    print_cities(session)

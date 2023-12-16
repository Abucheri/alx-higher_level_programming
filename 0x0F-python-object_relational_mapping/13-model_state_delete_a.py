#!/usr/bin/python3

"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine("mysql+mysqldb://{0}:{1}@localhost:3306/{2}"
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = (session.query(State).filter(State.name
                        .like("%a%")).all())
    for state in states_to_delete:
        session.delete(state)
    session.commit()

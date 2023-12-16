#!/usr/bin/python3

"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    mysql_username, mysql_password, db_name = (sys.argv[1], sys.argv[2],
                                               sys.argv[3])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, db_name))
    session = Session(engine)
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()

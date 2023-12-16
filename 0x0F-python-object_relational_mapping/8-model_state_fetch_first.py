#!/usr/bin/python3

"""
Script that prints the first State object from the database hbtn_0e_6_usa
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
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')
    session.close()

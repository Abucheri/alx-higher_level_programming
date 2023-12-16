#!/usr/bin/python3

"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database, state_name = (argv[1], argv[2],
                                                argv[3], argv[4])
    connection_settings = {
            'host': 'localhost',
            'port': 3306,
            'user': username,
            'passwd': password,
            'db': database,
            'charset': 'utf8'
    }
    engine = create_engine(
              "mysql+mysqldb://{user}:{passwd}@{host}:{port}/{db}".format(
                  **connection_settings))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()

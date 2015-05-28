import sqlite3
from settings import *
from cinema_hall import CinemaHall

connection = sqlite3.connect(database_cinema)
cursor = connection.cursor()

with open(sql_database, "r") as f:
    connection.executescript(f.read())
    connection.commit()

with open(sql_fill_database, "r") as f:
    cursor.executescript(f.read())
    connection.commit()

CinemaHall().create_hall()

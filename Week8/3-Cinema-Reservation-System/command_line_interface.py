from magic_reservation_system import MagicReservationSystem
from prepare_data_to_show import PrepareData

import sqlite3

class CLI:

    def __init__(self):
        self.db = sqlite3.connect("cinema.db")
        self.cursor = self.db.cursor()

    def enter_name(self, username):
            return username

    def enter_number_of_tickets(self, number_of_tickets):
            return number_of_tickets

    def choosen_movie(self, movie_id):
        movie = self.cursor.execute("SELECT movie_name, movie_rating\
                                     FROM Movies\
                                     WHERE movie_id = ?", (movie_id,))
        for elements in movie:
           return str(elements[0]) + " " + "({})".format(str(elements[1]))

    def choosen_date_and_time(self, projection_id):
        date_and_time = self.cursor.execute("SELECT movie_date, movie_time, movie_type\
                                     FROM Projections\
                                     WHERE projection_id = ?", (projection_id,))
        for elements in date_and_time:
            return str(elements[0]) + " " + str(elements[1]) + " " + "({})".format(str(elements[2]))

    def validate_projection(self, movie_id):
        valid_projection = self.cursor.execute("SELECT projection_id\
                                                FROM Projections\
                                                WHERE movie_id = ?", (movie_id,))
        id_list = []
        for id in valid_projection:
            for ids in id:
                id_list.append(ids)
        return id_list

    def choosen_seats(self, seat, projection_id):
        return seat





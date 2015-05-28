from magic_reservation_system import MagicReservationSystem
import sqlite3

class PrepareData:

    def __init__(self):
        self.db = sqlite3.connect("cinema.db")
        self.cursor = self.db.cursor()

    def print_show_movies(self):

        print("Current movies: ")
        for movies in MagicReservationSystem().show_movies():
            print("[{}]".format(movies[0]), movies[1], "({})".format(movies[2]))

    def print_show_movie_projections(self, movie_id):

        movie_name = self.cursor.execute("SELECT movie_name \
                                          FROM Movies \
                                          WHERE movie_id = ?", (movie_id,))
        title = ""
        for name in movie_name:
            title = name[0]
        projections_cursor = MagicReservationSystem().show_movie_projections(movie_id)
        if len(projections_cursor.fetchall()) == 0:
            message = "\nMovie with this id doesn't exist!"
            print(message)
            return
        print("Projections for movie '%s': " % title)
        for projections in MagicReservationSystem().show_movie_projections(movie_id):
            print("[{}]".format(projections[0]), projections[1], projections[2], "({})".format(projections[3]), projections[4], "available spots")


    def print_show_movie_projections_with_date(self, movie_id, movie_date):

        movie_name_date = self.cursor.execute("SELECT Movies.movie_name, Projections.movie_date \
                                               FROM Movies JOIN Projections \
                                               ON Movies.movie_id = ? AND Projections.movie_date = ?", (movie_id, movie_date,))
        m_name = ""
        m_date = ""
        for name_and_date in movie_name_date:
            m_name = name_and_date[0]
            m_date = name_and_date[1]
        print("Projections for movie '%s' on date '%s':" % (m_name, m_date))
        projections_cursor = MagicReservationSystem().show_movie_projections_with_date(movie_id, movie_date)
        if len(projections_cursor.fetchall()) == 0:
            message = "There are no projections for this movie on this date!"
            print(message)
            return
        for projections in MagicReservationSystem().show_movie_projections_with_date(movie_id, movie_date):
            print("[{}]".format(projections[0]), projections[1], "({})".format(projections[2]))

    def show_available_seats(self, projection_id):

            size_of_the_hall = MagicReservationSystem().show_cinema_hall(projection_id)
            every_row = ""
            print("Available seats (marked with a dot):")
            print("   1 2 3 4 5 6 7 8 9 10")

            for row, rows in enumerate(size_of_the_hall):
                for col, cols in enumerate(rows):
                    if col == 0 and row < 9:
                        every_row += str(row+1) + "  "
                    if col == 0 and row == 9:
                        every_row += str(row+1) + " "
                    every_row += str(cols) + " "
                print(every_row)
                every_row = ""





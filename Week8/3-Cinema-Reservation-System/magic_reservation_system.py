import sqlite3
import ast

class MagicReservationSystem:

    def __init__(self):
         self.connection = sqlite3.connect("cinema.db")
         self.cursor = self.connection.cursor()

    def show_movies(self):
        movies = self.cursor.execute("SELECT movie_id, movie_name, movie_rating \
                                      FROM Movies \
                                      ORDER BY movie_rating")
        return movies

    def show_movie_projections(self, movie_id):
            projections = self.cursor.execute("SELECT projection_id, movie_date, movie_time, movie_type, available_spots \
                                               FROM Projections \
                                               WHERE movie_id = ? \
                                               ORDER BY movie_date", (movie_id,))
            return projections

    def show_movie_projections_with_date(self, movie_id, movie_date):
        projections = self.cursor.execute("SELECT projection_id, movie_time, movie_type \
                                           FROM Projections \
                                           WHERE movie_id = ? AND movie_date = ?", (movie_id, movie_date,))
        return projections

    def show_cinema_hall(self, projection_id):

        cinema_hall = self.cursor.execute("SELECT cinema_hall \
                                           FROM CinemaHall \
                                           WHERE projection_id = ?", (projection_id,))
        for all_rows in cinema_hall:
             size_of_the_hall = all_rows[0]
        size_of_the_hall = ast.literal_eval(size_of_the_hall)
        return size_of_the_hall

    def available_spots_in_cinema(self, projection_id):

        cinema_hall = self.cursor.execute("SELECT cinema_hall \
                                           FROM CinemaHall \
                                           WHERE projection_id = ?", (projection_id,))
        available_spots = 0
        available_seats = "."
        taken_seats = "X"

        for all_rows in cinema_hall:
             size_of_the_hall = all_rows[0]
        size_of_the_hall = ast.literal_eval(size_of_the_hall)

        for r, rows in enumerate(size_of_the_hall):
            for c, cols in enumerate(rows):
               if size_of_the_hall[r][c] == available_seats:
                    available_spots += 1

        return available_spots


    def choose_seats(self, row, col, projection_id):

        cinema_hall = self.cursor.execute("SELECT cinema_hall \
                                           FROM CinemaHall \
                                           WHERE projection_id = ?", (projection_id,))
        for all_rows in cinema_hall:
             size_of_the_hall = all_rows[0]
        size_of_the_hall = ast.literal_eval(size_of_the_hall)

        if row > 10 or row < 1 or col > 10 or col < 1:
            print("\nThe seat doesn't exist!")
            return -1

        available_seats = "."
        taken_seats = "X"

        for row_, rows in enumerate(size_of_the_hall):
            if row_+1 == row:
                for col_, cols in enumerate(rows):
                     if col_+1 == col:
                         if size_of_the_hall[row_][col_] == taken_seats:
                                print("This seat is already taken!")
                                return -1
                         if size_of_the_hall[row_][col_] == available_seats:
                                size_of_the_hall[row_][col_] = taken_seats
                                print(str(size_of_the_hall))
                                self.cursor.execute("UPDATE CinemaHall \
                                                     SET cinema_hall = ?\
                                                     WHERE projection_id = ?", (str(size_of_the_hall), projection_id),)
                                self.connection.commit()


            else:
                continue




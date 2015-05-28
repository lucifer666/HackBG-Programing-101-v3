import sqlite3

class CinemaHall:

    def __init__(self):
       self.db = sqlite3.connect("cinema.db")
       self.cursor = self.db.cursor()

    def create_hall(self):

        create_hall = [
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        ]

        cinema_hall = str(create_hall)
        projection_id = 1
        len_of_all_rows = self.cursor.execute("SELECT COUNT(projection_id) \
                                               FROM Projections")
        count_rows_in_table_projections = 0

        for row in len_of_all_rows:
            count_rows_in_table_projections = row[0]

        while projection_id != count_rows_in_table_projections+1:
            self.cursor.execute("INSERT INTO CinemaHall(projection_id, cinema_hall) \
                                VALUES (%d, %r)" % (projection_id , cinema_hall))
            self.db.commit()
            projection_id += 1


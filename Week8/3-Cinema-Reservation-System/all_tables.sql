DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies(
    movie_id INTEGER PRIMARY KEY,
    movie_name TEXT,
    movie_rating REAL);

DROP TABLE IF EXISTS Projections;

CREATE TABLE Projections(
    projection_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    movie_type TEXT,
    movie_date TEXT,
    movie_time TEXT,
    available_spots INTEGER,
    FOREIGN KEY(movie_id) REFERENCES Movies(movie_id));

DROP TABLE IF EXISTS Reservations;

CREATE TABLE Reservations(
    reservation_id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY(projection_id) REFERENCES Projections(projection_id));

DROP TABLE IF EXISTS CinemaHall;

CREATE TABLE CinemaHall(
        cinema_hall TEXT,
        projection_id INTEGER,
        FOREIGN KEY(projection_id) REFERENCES Projections(projection_id));



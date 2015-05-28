INSERT INTO Movies(movie_name, movie_rating) VALUES
("Furious Seven", "7.8"),
("Avengers: Age of Ultron", "8.1"),
("Up", "8.3"),
("The Texas Chain Saw Massacre", "7.5"),
("Wrong Turn", "6.1"),
("The Silence of the Lambs", "8.1"),
("Dead Silence", "8.1"),
("Star Wars: Episode VII - The Force Awakens", "8.1"),
("Faster", "6.5"),
("Jumper", "6.1");


INSERT INTO Projections(movie_id, movie_type, movie_date, movie_time, available_spots) VALUES
(1, "2D", "2015-04-04", "19:10",100),
(1, "3D", "2015-04-04", "19:00",100),
(1, "4DX", "2015-04-05", "23:10",100),
(2, "4DX", "2015-04-01", "20:00",100),
(3, "2D", "2015-04-06", "17:00",100),
(3, "3D", "2015-04-06", "19:40",100),
(4, "3D", "2015-05-04", "15:00",100),
(4, "2D", "2015-05-04", "12:10",100),
(5, "2D", "2015-04-01", "23:00",100),
(6, "2D", "2015-04-07", "21:30",100),
(6, "3D", "2015-04-08", "21:40",100),
(7, "2D", "2015-05-05", "20:00",100),
(7, "2D", "2015-05-06", "22:00",100),
(8, "3D", "2015-04-06", "21:00",100),
(8, "4DX", "2015-04-06", "13:00",100),
(9, "2D", "2015-05-05", "20:00",100),
(9, "2D", "2015-05-06", "22:00",100),
(10, "2D", "2015-05-03", "11:00",100),
(10, "2D", "2015-05-04", "22:00",100),
(10, "3D", "2015-05-05", "15:00",100);


INSERT INTO Reservations(username, projection_id, row, col) VALUES
("Filip", 1, 9, 9),
("Katrin", 1, 9, 8),
("Ivan", 1, 5, 6),
("Georgi", 2, 7, 5),
("Georgi", 2, 7, 6),
("Pepi", 6, 4, 2),
("Pepi", 7, 5, 4),
("Spascho", 5, 2, 2),
("Mariika", 4, 1, 1),
("Unufri", 4, 3, 2);


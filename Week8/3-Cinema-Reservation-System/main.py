from magic_reservation_system import MagicReservationSystem
from prepare_data_to_show import PrepareData
from command_line_interface import CLI

def main():

    while True:

        print("\nWelcome to our cinema!\n")
        print("For Movies: Press 1")
        print("For Projections: Press 2")
        print("To make reservation: Press 3")
        print("For Help: Press 4")
        print("To Exit: Press 5")

        try:
            command = int(input("Please choose command>> "))

            if command < 1 or command > 5:
                print("\nWrong choice! Try again!")

            if command == 1:
                PrepareData().print_show_movies()

            elif command == 2:
                movie_id = int(input("Please choose movie id>> "))
                PrepareData().print_show_movie_projections(movie_id)

            elif command == 3:
                username = input("Choose name>> ")
                client_username = CLI().enter_name(username)

                number_of_tickets = int(input("Choose number of tickets>> "))
                client_tickets = CLI().enter_number_of_tickets(number_of_tickets)

                PrepareData().print_show_movies()

                movie_id = int(input("Please choose movie id>> "))
                client_movie = CLI().choosen_movie(movie_id)
                PrepareData().print_show_movie_projections(movie_id)

                projection_id = int(input("Please choose projection id>> "))
                if projection_id not in CLI().validate_projection(movie_id):
                    print("\nInvalid projection id!")
                    continue
                data_and_time_of_projection = CLI().choosen_date_and_time(projection_id)
                if client_tickets > MagicReservationSystem().available_spots_in_cinema(projection_id):
                    message = "\nThe tickets are more than the available spots in the cinema hall!"
                    print(message)
                    continue

                PrepareData().show_available_seats(projection_id)

                seats = ""
                while client_tickets != 0:
                    seat = tuple(int(x.strip()) for x in input("Choose seat: ").split(','))
                    #print(MagicReservationSystem().choose_seats(seat[0], seat[1], projection_id))
                    #seats += str(seat) + ","
                    #client_seats = CLI().choosen_seats(seats, projection_id)
                    print(MagicReservationSystem().choose_seats(seat[0], seat[1], projection_id))
                    MagicReservationSystem().choose_seats(seat[0], seat[1], projection_id)


                    client_tickets -= 1
                #print(client_seats)




            elif command == 4:
                print("\nFor movies - Show all movies in the cinema")
                print("For Projections - Show all projections for given movie")
                print("To make reservation - You can make reservations in our cinema")
                print("To Exit - You can exit from the system")

            elif command == 5:
                break

        except ValueError:
            print("\nPlease enter a valid value!")

if __name__ == "__main__":
    main()

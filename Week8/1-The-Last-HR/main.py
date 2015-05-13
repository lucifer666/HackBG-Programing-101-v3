from create_database  import Database
from fill_database import FillDatabase
from show_info import ShowInfo

def main():

        database = Database()
        filldatabase = FillDatabase()
        info = ShowInfo()
        database.create_database()
        filldatabase.fill_students_courses()
        filldatabase.fill_third_table()
        while True:
            print("\nIf you want to see:\n"
                  "1.All students with their GitHub accounts: press 1\n"
                  "2.The all courses: press 2\n"
                  "3.Each student with his courses: press 3\n"
                  "4.The students that have attented the most courses in Hack Bulgaria: press 4\n"
                  "5.If you want to exit: press 5")
            number = int(input("Command> "))

            if number<1 or number > 5:
                print("Wrong choise! Please try again!")


            if number == 1:
                result = info.student_with_git()
                for accounts in result:
                    if accounts[2] is not None and accounts[2] is not "":
                        if "github" in accounts[2]:
                            print(accounts[0], accounts[1], accounts[2])
            if number == 2:
                result = info.get_all_courses()
                for course in result:
                    print(course[0], course[1])

            if number == 3:
                result = info.students_and_courses()
                for student_courses in result:
                   print(student_courses[0], student_courses[1])

            if number == 4:
                result = info.students_with_the_most_courses()
                for students in result:
                    print(students[0], students[1])

            if number == 5:
                break

if __name__ == "__main__":
    main()

import sqlite3

class Database:

    def __init__(self):
        self.db = sqlite3.connect('/home/filip/exercisesHack/Week7.Day2/create_company.db')
        self.cursor = self.db.cursor()

    def create_database(self):
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS company(
                id INTEGER PRIMARY KEY,
                name TEXT,
                monthly_salary TEXT,
                yearly_bonus TEXT,
                position TEXT)''')
            self.db.commit()

    def insert_data(self):
        number_of_employees = int(input("How many employees do you want to add in the company: "))

        while number_of_employees != 0:
                name = input("Enter firstname and lastname: ")
                monthly_salary = int(input("Enter monthly_salary: "))
                yearly_bonus = int(input("Enter yearly_bonus: "))
                position = input("Enter position: ")

                self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))

                number_of_employees -= 1
                self.db.commit()
        print("The data were added successfuly!")



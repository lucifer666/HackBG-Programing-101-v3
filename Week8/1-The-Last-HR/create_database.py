import sqlite3

class Database:


    def __init__(self):
        self.db = sqlite3.connect("/home/filip/exercisesHack/Week8.Day1/student_and_courses.db")
        self.cursor = self.db.cursor()

    def create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY,
            github TEXT,
            available TEXT,
            student_name TEXT)''')
        self.db.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses(
            course_id INTEGER PRIMARY KEY,
            course_name TEXT)''')
        self.db.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses_with_students(
                student_id INTEGER,
                course_id INTEGER,
                group_ INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id),
                FOREIGN KEY(course_id) REFERENCES courses(course_id))''')
        self.db.commit()



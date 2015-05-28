from create_database  import Database
from fill_database import FillDatabase
import sqlite3

class ShowInfo:


    def __init__(self):
        self.db = sqlite3.connect('student_and_courses.db')
        self.cursor = self.db.cursor()

    def student_with_git(self):
        result = self.cursor.execute("SELECT student_id, student_name, github FROM students")
        return result

    def get_all_courses(self):
        result = self.cursor.execute("SELECT course_id, course_name FROM courses")
        return result

    def students_and_courses(self):
        result = self.cursor.execute("SELECT students.student_name, courses.course_name \
                                      FROM students JOIN courses ON courses.course_id IN (SELECT course_id \
                                      FROM courses_with_students WHERE students.student_id = courses_with_students.student_id)")
        return result

    def students_with_the_most_courses(self):

        result = self.cursor.execute("SELECT students.student_name, COUNT(courses_with_students.student_id)\
                                      FROM students JOIN courses_with_students\
                                      ON students.student_id = courses_with_students.student_id\
                                      WHERE students.student_id IN (\
                                      SELECT student_id\
                                      FROM courses_with_students\
                                      GROUP BY student_id\
                                      ORDER BY COUNT(*) DESC\
                                      LIMIT 1)")
        return result



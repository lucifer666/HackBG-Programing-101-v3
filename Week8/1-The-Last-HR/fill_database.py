from create_database import Database
import requests
import sqlite3

class FillDatabase:

    def __init__(self):
        self.url = "https://hackbulgaria.com/api/students/"
        self.db = sqlite3.connect('/home/filip/exercisesHack/Week8.Day1/student_and_courses.db')
        self.cursor = self.db.cursor()
        self.json_content = {}


    def get_api_info(self):
        request = requests.get(self.url)
        content = request.json()
        return content

    def fill_students_courses(self):
        self.json_content = self.get_api_info()
        courses_list = []

        for students in self.json_content:
            self.cursor.execute('''INSERT INTO students(github, available, student_name) VALUES(?,?,?)''', (students["github"],students["available"],
                students["name"]))
            self.db.commit()
            for course in students["courses"]:
                courses_list.append(course["name"])

        all_courses = set(courses_list)
        for course in all_courses:
             self.cursor.execute('''INSERT INTO courses(course_name) VALUES(?)''', (course,))
             self.db.commit()

    def fill_third_table(self):
        self.json_content = self.get_api_info()

        for s_id, students in enumerate(self.json_content):
            stud_id = self.cursor.execute("SELECT student_id FROM students WHERE student_id=?", (s_id+1,))


            for st_id in stud_id:
                for course in students["courses"]:
                    cour_id = self.cursor.execute("SELECT course_id FROM courses WHERE course_name=?", (course["name"],))
                    for co_id in cour_id:
                        self.cursor.execute('''INSERT INTO courses_with_students(student_id, course_id, group_) VALUES(?,?,?)''',
                        (st_id[0],co_id[0], course["group"],))
                        self.db.commit()












import sqlite3

class Database:


    def __init__(self):
        self.db = sqlite3.connect("all_links.db")
        self.cursor = self.db.cursor()

    def create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS links(
            link TEXT)''')
        self.db.commit()



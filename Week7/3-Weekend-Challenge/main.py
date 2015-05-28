import sqlite3
from crawl import Crawler
from create_database_with_links import Database

def main():
    crawler = Crawler("http://start.bg/")
    database = Database()
    crawler.start()




if __name__ == "__main__":
    main()

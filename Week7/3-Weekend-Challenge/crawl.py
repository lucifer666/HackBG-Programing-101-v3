import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, url):
        self.url = url
        self.internal_links = []
        self.external_links = []
        self.visited = []

    def start(self):
        links = self.get_links_from_url(self.url)
        self.classify(links)
        self.visited.append(self.url)
        count = 0
        for link in self.internal_links:
            print(link)
            if link not in self.visited:
                self.visited.append(link)
                sub_pages = self.get_links_from_url(link)
                self.classify(sub_pages)

    def get_links_from_url(self, url):
        try:
            request = requests.get(url, timeout=2)
            soup = BeautifulSoup(request.text)

            links = []
            for link in soup.find_all('a'):
                links.append(link.get('href'))


        except:
            return("Invalid url!")

        return links

    def classify(self, links):

            for link in links:
                if link is None:
                    continue
                if "start.bg" in link:
                    self.internal_links.append(link)
                elif "link.php?" in link:
                    self.external_links.append(link)

            return self.internal_links




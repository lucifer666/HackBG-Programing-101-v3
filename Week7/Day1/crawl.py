from bs4 import BeautifulSoup
from histogram import Histogram
import requests
import json

class CrawlBgWeb:

    def __init__(self):
        self.url = "http://register.start.bg/"
        self.list_of_links = []

    def get_html(self):
        request = requests.get(self.url)
        return request

    def parse_html(self):

        soup = BeautifulSoup(self.get_html().content)
        links = soup.find_all('a')
        try:
            for link in links:
                self.list_of_links.append(link.get('href'))
            return  self.list_of_links
        except KeyError:
            pass

    def get_headers(self):

        all_links = self.parse_html()
        server_names = ["Apache", "nginx", "OpenSSL", "Microsoft-IIS"]
        histogram = Histogram()

        for link in all_links:
            try:
                if link is not None and "link.php?id=" in link:
                    req = requests.head(self.url + link, timeout=2, allow_redirects=True)
                    get_server = req.headers["Server"]
                    print(get_server)
                    for servers in server_names:
                        if servers in get_server:
                            get_server = servers
                            histogram.add(get_server)
                            break
                        if servers == server_names[-1]:
                            get_server = "other servers"
                            histogram.add(get_server)
            except Exception:
               print("The page is not responding...")
               continue
        return histogram


    def save_histogram(self, histogram):

            with open("servers.json", "w") as f:
                json.dump(histogram, f, indent=4)


    def load_histogram(self,filename):

        with open(filename, "r") as f:
            data = json.loads(f.read())
            return data





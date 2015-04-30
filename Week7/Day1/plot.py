import matplotlib.pyplot as plt
from histogram import Histogram
from crawl import CrawlBgWeb


class Chart:

    def make_chart(self):
        crawl = CrawlBgWeb()
        dict_histogram = crawl.load_histogram("servers.json")
        labels = []
        sizes = []
        for servers in dict_histogram:
            labels.append(servers)
            sizes.append(dict_histogram[servers])

        colors = ['yellow', 'pink', 'red', 'green']
        explode = (0.1, 0.1, 0.1, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')

        plt.show()



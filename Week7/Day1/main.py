from plot import Chart
from crawl import CrawlBgWeb
from histogram import Histogram



def main():
    chart = Chart()
    crawl = CrawlBgWeb()
    crawl.parse_html()
    histogram = crawl.get_headers().get_dict()
    crawl.save_histogram(histogram)
    crawl.load_histogram("servers.json")
    chart.draw_chart()

if __name__ == "__main__":
    main()

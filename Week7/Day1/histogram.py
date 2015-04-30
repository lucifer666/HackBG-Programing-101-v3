
class Histogram:

    def __init__(self):
        self.dict_servers = {}
        self.list_servers = []

    def add(self, server):
        self.list_servers.append(server)


    def count(self, server):
        if server  not in self.list_servers:
            return None
        count_server = self.list_servers.count(server)
        return count_server

    def get_dict(self):
       for server in self.list_servers:
            self.dict_servers[server] = self.count(server)
       return self.dict_servers
"""
def main():
    h = Histogram()
    h.add("Apache")
    h.add("Apache")
    h.add("nginx")
    h.add("IIS")
    h.add("nginx")
    print(h.count("Apache"))
    print(h.count("nginx"))
    print(h.count("IIS"))
    print(h.count("IBM Web Server"))
    #print(h.get_dict())

    if __name__ == "__main__":
    main()
"""

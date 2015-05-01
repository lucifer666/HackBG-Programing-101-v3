
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

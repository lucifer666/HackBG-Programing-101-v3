import json
from class_panda import Panda

class PandaAlreadyThere(Exception):
    pass
class PandasAlreadyFriends(Exception):
    pass

class PandaSocialNetwork:

    def __init__(self, panda_dict):
        self.panda_dict = panda_dict


    def add_panda(self, panda):

        if panda in self.panda_dict:
            raise PandaAlreadyThere
        else:
            self.panda_dict[panda] = []

    def has_panda(self, panda):
        for pandas in self.panda_dict:
            if panda == pandas:
                return True
        return False

    def make_friends(self, panda1, panda2):

        if panda1 not in self.panda_dict:
            self.panda_dict[panda1] = []
        if panda2 not in self.panda_dict:
            self.panda_dict[panda2] = []

        if panda1 not in self.panda_dict[panda2] and panda2 not in self.panda_dict[panda1]:
            self.panda_dict[panda1].append(panda2)
            self.panda_dict[panda2].append(panda1)
        else:
            raise PandasAlreadyFriends

    def are_friends(self, panda1, panda2):
        if panda1 in self.panda_dict and panda2 in self.panda_dict:
            if panda1 in self.panda_dict[panda2] and panda2 in self.panda_dict[panda1]:
                return True
        return False

    def friend_of(self,panda):
        if panda not in self.panda_dict:
            return False
        return self.panda_dict[panda]


    def search_friends(self, start, end):

        visited = set()
        path_to = {}
        queue = []
        visited.add(start)
        queue.append(start)
        path_to[start] = None
        found = False
        path_length = 0
        if self.has_panda(start) == False or self.has_panda(end) == False:
            return False
        if start in self.panda_dict[end] and end in self.panda_dict[start]:
            return 1
        while len(queue) != 0:

            current_node = queue.pop(0)
            if current_node == end:
                found = True
                break
            for neighbour in self.panda_dict[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)

        if found == True:
            while path_to[end] is not None:
                path_length += 1
                end = path_to[end]
            #print(json.dumps(path_to, sort_keys=True, indent=4)) # this is for check
            return path_length
        return -1 # if the pandas are not connected at all


    def connection_level(self, panda1, panda2):

        return self.search_friends(panda1, panda2)

    def are_connected(self, panda1, panda2):
        if self.search_friends(panda1, panda2) == False:
            return False
        elif self.search_friends(panda1, panda2) == -1:
            return False
        else:
            return True

    def how_many_gender_in_network(self, level, panda, gender):

        if level < 1:
            raise Exception("The level is not correct!")

        count_gender = 0
        for current_panda in self.panda_dict:
            if self.connection_level(panda, current_panda) is not False and self.connection_level(panda, current_panda) != -1:
                current_connection_level = self.connection_level(panda, current_panda)
                if current_panda != panda and current_connection_level <= level and current_panda.gender() == gender:
                    count_gender += 1

        return count_gender

    def prepare_to_json(self):
        network_dict = {}
        for panda in self.panda_dict:
            network_dict[panda.name()] = [friends.name() for friends in self.panda_dict[panda]]
        return network_dict


    @staticmethod
    def save_social_network(network):

        fwrite = open("social_network.json", "w")
        json.dump(network, fwrite, indent=True)
        fwrite.close()

    @staticmethod
    def load_social_network(filename):
        list_network = []
        with open(filename, "r") as f:
            data = json.loads(f.read())

            network = PandaSocialNetwork(data)
            for members in data:
                if len(data[members]) == 1:
                    for friends in data[members]:
                        content = "%s have one friend - %s" %(members, friends)
                        list_network.append(content)
                if len(data[members]) > 1:
                    content = "The friends of %s are - " % (members)
                    for friends in data[members]:
                        if friends == data[members][-1]:
                            content +=  "%s" % (friends)
                            break
                        content +=  "%s," % (friends)
                    list_network.append(content)
            return list_network



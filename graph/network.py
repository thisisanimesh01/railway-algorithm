import networkx as nx

class RailwayNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_station(self, station):
        self.graph.add_node(station)

    def add_track(self, s1, s2, distance):
        self.graph.add_edge(s1, s2, weight=distance)

    def get_neighbors(self, station):
        return list(self.graph.neighbors(station))

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target, weight='weight')
from GraphData import graph

graph = graph

class Graph:

    def __init__(self, graph: dict = {}):
        self.graph = graph# dictionary for adjacency list

    # def add_edge(self, star1, star2, weight):
    #     if star1 not in self.graph:
    #         self.graph[star1] = {}
    #     self.graph[star1][star2] = weight

    def shortest_distances(self, source: str):
        distances = {star: float("inf") for star in self.graph}
        distances[source] = 0

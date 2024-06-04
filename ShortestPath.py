from GraphDictionary import graph
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph  # dictionary for adjacency list

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {star: float("inf") for star in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Priority queue to store the nodes to explore
        priority_queue = [(0, source)]
        heapify(priority_queue)

        while priority_queue:
            current_distance, current_node = heappop(priority_queue)

            # Skip if we've already found a shorter path
            if current_distance > distances[current_node]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))

        return distances

G = Graph(graph = graph)

#find the shortest paths from star
star_source = input("input the star source: \n")
distances = G.shortest_distances(star_source)

where = input("to where: \n")

to_where = distances[where]
print(f"The shortest distance from {star_source} to {where} is {to_where}")

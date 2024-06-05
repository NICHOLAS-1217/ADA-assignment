from GraphDictionary import graph
from heapq import heapify, heappop, heappush

class Graph:

    def __init__(self, graph: dict = {}):
        self.graph = graph # dictionary for adjacency list

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {star: float("inf") for star in self.graph}
        distances[source] = 0  # Set the source value to 0
        # Dictionary to store the shortest path tree
        predecessors = {star: None for star in self.graph}
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
                    predecessors[neighbor] = current_node
                    heappush(priority_queue, (distance, neighbor))
        return distances, predecessors
    
    def get_shortest_path(self, predecessors, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        return path if path[0] == start else []

G = Graph(graph = graph)

with open('ShortestPath.txt', 'w') as file:
    for i in range(20):
        from_star = 'A'
        shortest_distances, predecessors = G.shortest_distances(from_star)
        to_star = chr(65 + i)  # Convert to character (A, B, C, D)
        distance = shortest_distances[to_star]
        file.write(f"The shortest distance from {from_star} to {to_star} is {distance}\n")
        path = G.get_shortest_path(predecessors, from_star, to_star)
        file.write("The shortest path:\n")
        file.write(" -> ".join(path) + "\n")

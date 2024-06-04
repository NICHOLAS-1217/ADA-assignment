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

# representing graph in dictionary
graph = {
    "D": {
        "I": 416.72,
        "H": 523.18,
        "C": 519.05,
        "N": 577.21,
        "S": 521.11,
    },
    "I": {
        "K": 366.68,
        "B": 668.08,
        "A": 382.44,
        "H": 432.05,
        "D": 416.72,
    },
    "K": {
        "O": 391.54,
        "F": 283.38,
        "B": 712.28,
        "I": 366.68,
    },
    "G": {
        "P": 935.88,
        "J": 73.10,
        "O": 461.92,
    },
    "N": {
        "D": 577.21,
        "H": 726.06,
        "C": 725.44,
        "Q": 906.68,
    },
    "H": {
        "I": 432.05,
        "A": 99.37,
        "M": 566.99,
        "C": 7.14,
        "N": 726.06,
        "D": 523.18
    },
    "B": {
        "K": 712.28,
        "O": 487.96,
        "F": 509.58,
        "L": 609.81,
        "A": 791.26,
        "I": 668.08
    },
    "O": {
        "G": 461.92,
        "J": 465.21,
        "T": 511.05,
        "F": 112.66,
        "B": 487.96,
        "K": 391.54
    },
    "C": {
        "D": 519.05,
        "H": 7.14,
        "A": 104.58,
        "M": 562.77,
        "S": 95.21,
        "N": 725.44
    },
    "A": {
        "I": 382.44,
        "B": 791.26,
        "F": 361.62,
        "L": 905.38,
        "E": 662.30,
        "M": 582.76,
        "C": 104.58,
        "H": 99.37
    },
    "F": {
        "K": 283.38,
        "O": 112.66,
        "T": 405.11,
        "R": 313.80,
        "L": 667.89,
        "A": 361.82,
        "B": 509.58
    },
    "J": {
        "G": 73.10,
        "P": 986.62,
        "T": 314.31,
        "O": 465.21,
    },
    "Q": {
        "N": 906.68,
        "M": 452.15,
        "S": 613.36,
    },
    "M": {
        "H": 566.99,
        "A": 582.76,
        "L": 670.93,
        "S": 554.37,
        "Q": 452.15,
        "C": 562.77
    },
    "L": {
        "B": 609.81,
        "F": 667.89,
        "T": 845.76,
        "R": 637.49,
        "E": 650.27,
        "M": 670.93,
        "A": 905.38
    },
    "T": {
        "O": 511.05,
        "J": 314.31,
        "P": 776.85,
        "R": 653.81,
        "L": 845.76,
        "F": 405.11
    },
    "S": {
        "C": 95.21,
        "M": 554.37,
        "E": 635.58,
        "Q": 613.36,
        "D": 521.11,
    },
    "E": {
        "A": 662.30,
        "L": 650.27,
        "R": 994.52,
        "S": 635.58
    },
    "R": {
        "F": 313.80,
        "T": 653.81,
        "P": 525.79,
        "E": 994.52,
        "L": 637.49,
    },
    "P": {
        "J": 986.62,
        "G": 935.88,
        "R": 525.79,
        "T": 776.85,
    }
}

G = Graph(graph=graph)

#find the shortest paths from star
star_source = input("input the star source: \n")
distances = G.shortest_distances(star_source)

where = input("to where: \n")

to_where = distances["F"]
print(f"The shortest distance from {star_source} to {where} is {to_where}")

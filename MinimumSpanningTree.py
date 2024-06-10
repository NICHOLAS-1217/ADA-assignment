from GraphDictionary import graph  

class Graph:  
    def __init__(self, vertices):  
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store the graph

    def addEdge(self, u, v, w):  
        # Function to add an edge to the graph
        self.graph.append([u, v, w])  

    def find(self, parent, i):  
        # Function to find the set of an element i (uses path compression technique)
        if parent[i] != i:   
            parent[i] = self.find(parent, parent[i])  
        return parent[i]  

    def union(self, parent, rank, x, y):  
        # Function that does union of two sets of x and y (uses union by rank)
        if rank[x] < rank[y]:  
            parent[x] = y  
        elif rank[x] > rank[y]:  
            parent[y] = x  
        else:  
            parent[y] = x  
            rank[x] += 1 

    def KruskalMST(self, graph_dict):  
        result = []  # This will store the resultant MST
        i = 0  # Variable for sorted edges
        e = 0  # Variable to keep count of edges included in MST

        # Convert the graph dictionary into a list of edges
        edges = [] 
        for u, neighbors in graph_dict.items(): 
            for v, weight in neighbors.items(): 
                edges.append((u, v, weight)) 

        # Sort all the edges in non-decreasing order of their weight
        edges = sorted(edges, key=lambda item: item[2]) 

        # Create subsets with single elements
        parent = {}  
        rank = {}  
        for node in graph_dict.keys():  
            parent[node] = node 
            rank[node] = 0 

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:  
            # Pick the smallest edge and increment the index for next iteration
            u, v, w = edges[i]  
            i = i + 1 

            x = self.find(parent, u)  
            y = self.find(parent, v)  

            # If including this edge does not cause cycle, include it in result
            # and increment the index of the result for the next edge
            if x != y:  
                e = e + 1 
                result.append([u, v, w])  
                self.union(parent, rank, x, y)  

        minimumCost = 0 
        output_lines = ["Edges in the constructed MST"] 
        for u, v, weight in result:  
            minimumCost += weight  
            output_lines.append(f"{u} -- {v} == {weight}") 
        output_lines.append(f"Minimum Spanning Tree weight: {round(minimumCost, 2)}") 

        return output_lines 

# Create a graph instance with the number of vertices
g = Graph(len(graph)) 

# Generate the MST using Kruskal's algorithm
output_lines = g.KruskalMST(graph) 

# Write the output to a file
with open("MinimumSpanningTree.txt", "w") as file: 
    for line in output_lines: 
        file.write(line + "\n") 



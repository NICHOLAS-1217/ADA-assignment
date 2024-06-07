from GraphDictionary import graph

class Graph: 
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
  
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
  
    def find(self, parent, i): 
        if parent[i] != i:  
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 
   
    def union(self, parent, rank, x, y): 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
        else: 
            parent[y] = x 
            rank[x] += 1
  
    def KruskalMST(self, graph_dict): 
        result = [] 
        i = 0
        e = 0
        edges = []
        for u, neighbors in graph_dict.items():
            for v, weight in neighbors.items():
                edges.append((u, v, weight))
        edges = sorted(edges, key=lambda item: item[2])
        parent = {} 
        rank = {} 
        for node in graph_dict.keys(): 
            parent[node] = node
            rank[node] = 0
        while e < self.V - 1: 
            u, v, w = edges[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
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

g = Graph(len(graph))

output_lines = g.KruskalMST(graph)

with open("MinimumSpanningTree.txt", "w") as file:
    for line in output_lines:
        file.write(line + "\n")


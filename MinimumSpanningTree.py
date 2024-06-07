from GraphDictionary import graph

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    # Convert the graph into a list of edges with weights
    edges = []
    nodes = list(graph.keys())
    node_index = {node: i for i, node in enumerate(nodes)}

    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((weight, node, neighbor))

    # Sort the edges based on their weights
    edges.sort()

    uf = UnionFind(len(nodes))

    mst = []
    total_weight = 0

    for weight, u, v in edges:
        u_index = node_index[u]
        v_index = node_index[v]

        if uf.find(u_index) != uf.find(v_index):
            uf.union(u_index, v_index)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Execute Kruskal's algorithm
mst, total_weight = kruskal(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print(f"Total weight: {total_weight}")

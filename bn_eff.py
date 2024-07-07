import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self, num_nodes):
        self.adj_list = {i: [] for i in range(num_nodes)}
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def neighbors(self, node):
        return self.adj_list[node]
    
    def nodes(self):
        return list(self.adj_list.keys())

def bfs_burn(graph, start_nodes):
    """
    Simulate the burning process on the graph starting from the start_nodes.
    """
    burned = set(start_nodes)
    frontier = set(start_nodes)
    round = 0
    
    while len(burned) < len(graph.nodes()):
        next_frontier = set()
        for node in frontier:
            neighbors = set(graph.neighbors(node))
            next_frontier.update(neighbors - burned)
        
        burned.update(next_frontier)
        frontier = next_frontier
        round += 1
        
        if not frontier:
            break
    
    return round

def find_burning_number(graph):
    """
    Find the burning number of the graph by trying different start nodes combinations.
    """
    min_rounds = float('inf')
    best_start_nodes = []
    
    nodes = graph.nodes()
    n = len(nodes)
    
    for i in range(n):
        for j in range(i, n):
            start_nodes = [nodes[i], nodes[j]]
            rounds = bfs_burn(graph, start_nodes)
            if rounds < min_rounds:
                min_rounds = rounds
                best_start_nodes = start_nodes
    
    return min_rounds, best_start_nodes

# Example usage:
num_nodes = 10
edge_probability = 0.3

# Create a random graph
graph = Graph(num_nodes)
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < edge_probability:
            graph.add_edge(i, j)

rounds, start_nodes = find_burning_number(graph)
print(f"Minimum rounds: {rounds}, Best start nodes: {start_nodes}")

# Visualize the graph
def plot_graph(graph):
    pos = {i: (random.uniform(0, 1), random.uniform(0, 1)) for i in graph.nodes()}
    plt.figure(figsize=(8, 8))
    for node, neighbors in graph.adj_list.items():
        for neighbor in neighbors:
            x_values = [pos[node][0], pos[neighbor][0]]
            y_values = [pos[node][1], pos[neighbor][1]]
            plt.plot(x_values, y_values, 'gray')
    for node in graph.nodes():
        plt.scatter(pos[node][0], pos[node][1], c='skyblue', s=100)
        plt.text(pos[node][0], pos[node][1], str(node), fontsize=12, ha='center', va='center')
    plt.show()

plot_graph(graph)

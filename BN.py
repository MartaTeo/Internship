# Auxiliary functions

def vertices_radius(graph, center, radius):
        """
        Get all vertices within a given radius from the center vertex.
        
        Parameters:
        graph (dict): The input graph as an adjacency list.
        center (int): The center vertex.
        radius (int): The radius.
        
        Returns:
        set: A set of vertices within the given radius from the center.
        """
        current_level = [center]
        visited = set(current_level)
        
        for _ in range(radius):

            next_level = set()

            for vertex in current_level:
                for neighbor in graph[vertex]:
                    if neighbor not in visited:

                        next_level.add(neighbor)

            visited.update(next_level)
            current_level = next_level
        
        return visited
    


# Greedy burning

def greedy_burning(G):
    """
    Parameters:
    G (dict): The input graph as an adjacency list.

    Returns:
    int: The number of steps (r) required to cover all vertices.
    """

    r = 0
    uncovered_vertices = set(G.keys())

    while uncovered_vertices:
        v = uncovered_vertices.pop()
        
        vertices_within_radius = vertices_radius(G, v, r) # Ball centered at v of radius r
        
        uncovered_vertices -= vertices_within_radius # Covered vertices
        
        r += 1
    
    return r



# Random Greedy Algorithm

import random

def random_greedy_burning(G, m):
    """
    Parameters:
        graph (dict): The input graph as an adjacency list.
        m (int): The maximum radius for the ball.

        Returns:
        int: The number of steps (t) required to cover all vertices.
    """

    t = 0
    uncovered_vertices = set(G.keys())

    while uncovered_vertices:
            v = uncovered_vertices.pop() 
            
            rt = random.randint(0, m) # random radius
            
            vertices_within_radius = vertices_radius(G, v, rt) # Ball
            
            uncovered_vertices -= vertices_within_radius
            
            t += 1
        
    return t








# Testing

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [4]
}

# Greedy Algorithm
bn = greedy_burning(graph)
print(f"Greedy: {bn}")

# Random Greedy Algorithm
bn = random_greedy_burning(graph, 3)
print(f'Random Greedy: {bn}')
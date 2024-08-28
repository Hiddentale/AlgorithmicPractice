import random

def generate_random_undirected_graph(num_vertices=10):
    graph = {}
    
    for i in range(num_vertices):
        graph[i] = set()
    
    for _ in range(5 * num_vertices):  # Add approximately 5 times the number of vertices
        v1 = random.randint(0, num_vertices - 1)
        v2 = random.randint(0, num_vertices - 1)
        
        # Ensure v1 != v2 and they're not already connected
        while v1 == v2 or (v1, v2) in [(str(x), str(y)) for x in graph.keys() for y in graph[x]]:
            v2 = random.randint(0, num_vertices - 1)
        
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    return graph
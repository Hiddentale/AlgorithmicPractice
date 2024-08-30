from queue import Queue
from graph_generator import generate_random_undirected_graph

def BreadthFirstSearch(graph, entry_node):

    queue = Queue()
    queue.put(entry_node)

    visited = set()
    visited.add(entry_node)

    while queue.qsize() > 0:
        current_node = queue.get()
        for edge in graph[current_node]:
            if edge not in visited:
                visited.add(edge)
                queue.put(edge)

def main():
    random_graph = generate_random_undirected_graph(5)
    print(random_graph)

    for vertex, neighbors in random_graph.items():
        print(f"{vertex} -> {neighbors}")

    BreadthFirstSearch(random_graph, 0)

main()
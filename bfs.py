from queue import Queue
from graph_generator import generate_random_undirected_graph

def BreadthFirstSearch(graph, entry_node):
    lengths_dict = {}
    lengths_dict[entry_node] = 0

    queue = Queue()
    queue.put(entry_node)
    explored = set()
    explored.add(entry_node)

    while queue.qsize() > 0:
        node = queue.get()
        for edge in graph[node]:
            if edge not in explored:
                lengths_dict[edge] = lengths_dict[node] + 1
                explored.add(edge)
                queue.put(edge)
    print(f"Lengths_dict: {lengths_dict}")

def main():
    random_graph = generate_random_undirected_graph(5)
    print(random_graph)

    for vertex, neighbors in random_graph.items():
        print(f"{vertex} -> {neighbors}")

    BreadthFirstSearch(random_graph, 0)

main()
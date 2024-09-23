from collections import defaultdict

def construct_path(graph):
    
    path = []
    edge_dictionary = defaultdict(list[int])
    edge_visited = set()

    for node_edge in graph:
        current_node, adjacent_node = node_edge[0], node_edge[1]
        edge_dictionary[current_node].append(adjacent_node)
        edge_dictionary[adjacent_node].append(current_node)

    def depth_first_search(current_node):
        for adjacent_node in edge_dictionary[current_node]:
            edge = tuple(sorted((current_node, adjacent_node)))
            if edge not in edge_visited:
                edge_visited.add(edge)
                path.append((current_node, adjacent_node))
                depth_first_search(adjacent_node)
                path.append((adjacent_node, current_node))
                
    depth_first_search(graph[0][0])
    return path

input = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (4, 5),
    (3, 5)
]

print(construct_path(input))


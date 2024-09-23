from collections import defaultdict

def find_universal_sink(adjacency_list):

    nodes = set(adjacency_list.keys())
    for neighbours in adjacency_list.values():
        nodes.update(neighbours)
    
    node_in_degree = defaultdict(int)
    node_out_degree = defaultdict(int)
    visited = defaultdict(lambda: False)

    def dfs(current_node):
        visited[current_node] = True
        if current_node in adjacency_list:
            for adjacent_node in adjacency_list[current_node]:
                node_in_degree[adjacent_node] += 1
                node_out_degree[current_node] += 1
                if visited[adjacent_node] != True:
                    dfs(adjacent_node)

    for node in adjacency_list.keys():
        if visited[node] == False:
            dfs(node)

    for key, value in node_in_degree.items():
        if value == len(nodes) - 1:
            if key not in node_out_degree:
                return f"Universal sink detected at node {key}!"
                
    return "No universal sink detected!"

adjacency_list = {
    'A': ['B', 'D', 'E'],
    'B': ['C', 'D', 'E'],
    'C': ['B', 'D'],
    'E': ['D']
}

print(find_universal_sink(adjacency_list))

def find_universal_sink_matrix(adjacency_matrix):

    possible_sinks = []

    for index in range(len(adjacency_matrix)):
        if adjacency_matrix[index] == [0] * len(adjacency_matrix):
            possible_sinks.append(index)

    if len(possible_sinks) > 1:
        return "No universal sink detected!"
    
    for index in range(len(adjacency_matrix)):
        if index != possible_sinks[0]:
            if adjacency_matrix[index][possible_sinks[0]] != 1:
                return "No universal sink detected!"
    return "Universal sink detected!"

adjacency_matrix = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

print(find_universal_sink_matrix(adjacency_matrix))
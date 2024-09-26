from collections import defaultdict
from queue import PriorityQueue

def find_shortest_path(graph, edge_weights, starting_node, end_destination, total_range_of_car):
    edge_dictionary = defaultdict(list)
    for element in graph:
        current_node, adjacent_node = element[0], element[1]
        edge_dictionary[current_node].append(adjacent_node) 
        
    edge_weight_dictionary = defaultdict(int)    
    for connection in edge_weights:
        edge, weight = connection[0], connection[1]
        if weight > total_range_of_car:
            edge_dictionary[edge[0]].remove(edge[1])
            continue
        edge_weight_dictionary[edge] = weight
        
    path_lengths_dict = defaultdict(int)
    print(edge_dictionary)
    
    def breadth_first_search(starting_node):
        queue = PriorityQueue()
        for adjacent_node in edge_dictionary[starting_node]:
            edge = (starting_node, adjacent_node)
            edge_weight = edge_weight_dictionary[edge]
            print((edge_weight, (edge, 0)))
            queue.put((edge_weight, (edge, 0)))
        
        while queue.qsize() > 0:
            (edge_weight, (edge, length_to_previous_node)) = queue.get()
            #print((edge_weight, (edge, length_to_previous_node)))
            distance_to_current_node = length_to_previous_node + edge_weight
            current_node = edge[1]
            #print(current_node)
            if current_node == end_destination:
                return distance_to_current_node
            path_lengths_dict[(starting_node, current_node)] = distance_to_current_node
            #print(path_lengths_dict)
            
            if current_node in edge_dictionary:
                for adjacent_node in edge_dictionary[current_node]:
                    edge = (current_node, adjacent_node)
                    adjacent_node_edge_weight = edge_weight_dictionary[edge]
                    print((adjacent_node_edge_weight, (edge, distance_to_current_node)))
                    queue.put((adjacent_node_edge_weight, (edge, distance_to_current_node)))
        return False
    
    return breadth_first_search(starting_node)

graph = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
edge_weights = [((0, 1), 50), ((0, 2), 100), ((1, 3), 75), ((2, 3), 25), ((3, 4), 50)]
starting_node = 0
ending_node = 4
total_range_of_car = 100
new_possible_edges = [(0, 3), (1, 4), (2, 4)]
new_possible_edge_weights = [((0, 3), 90), ((1, 4), 80), ((2, 4), 70)]

current_shortest_path = find_shortest_path(graph, edge_weights, starting_node, ending_node, total_range_of_car)
possible_new_edge = None
for index in range(len(new_possible_edges)):
    new_graph = graph + [new_possible_edges[index]]
    new_edges = edge_weights + [new_possible_edge_weights[index]]
    shortest_path = find_shortest_path(new_graph, new_edges, starting_node, ending_node, total_range_of_car)
    if shortest_path != False and shortest_path < current_shortest_path:
        current_shortest_path = shortest_path
        possible_new_edge = new_possible_edge_weights[index]
           
if possible_new_edge != None:
    print(f"If we add {possible_new_edge}, we get a shorter path from {starting_node} to {ending_node}!")
else:
    print("Current path was already shortest path.")
        

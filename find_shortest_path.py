from collections import defaultdict
from queue import PriorityQueue

def find_shortest_path(graph, edge_weights, start_destination, end_destination, total_range_of_car):
    edge_dictionary = defaultdict(list)
    for element in graph:
        current_node, adjacent_node = element[0], element[1]
        edge_dictionary[current_node].append(adjacent_node) 
        
    edge_weight_dictionary = defaultdict(int)    
    for connection in edge_weights:
        edge, weight = connection[0], connection[1] #Edge is (0,1) format
        if weight > total_range_of_car:
            edge_dictionary[edge[0]].remove(edge[1])
            continue
        edge_weight_dictionary[edge] = weight
        
    path_lengths_dict = defaultdict(int)
    
    def breadth_first_search(start_destination):
        queue = PriorityQueue() # will be of the form (weight, edge)
        for adjacent_node in edge_dictionary[start_destination]:
            edge = (start_destination, adjacent_node)
            edge_weight = edge_weight_dictionary[edge]
            queue.put((edge_weight, (edge, 0)))
        
        while queue.qsize() > 0:
            (edge_weight, (edge, length_to_previous_node)) = queue.get()
            distance_to_current_node = length_to_previous_node + edge_weight
            current_node = edge[1]
            if current_node == end_destination:
                return f"Minimum distance between {start_destination} and {end_destination} is: {distance_to_current_node}"
            path_lengths_dict[(start_destination, current_node)] = distance_to_current_node
            
            if current_node in edge_dictionary:
                for adjacent_node in edge_dictionary[current_node]:
                    edge = (current_node, adjacent_node)
                    adjacent_node_edge_weight = edge_weight_dictionary[edge]
                    queue.put((adjacent_node_edge_weight, (edge, distance_to_current_node)))
        return "No path available"
    
    return breadth_first_search(start_destination)

graph = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
edge_weights = [((0, 1), 50), ((0, 2), 100), ((1, 3), 75), ((2, 3), 25), ((3, 4), 50)]
start_destination = 0
end_destination = 4
total_range_of_car = 100

print(find_shortest_path(graph, edge_weights, start_destination, end_destination, total_range_of_car))

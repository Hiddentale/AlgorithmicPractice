from collections import defaultdict
from queue import Queue

def path_exists(graph, edge_weights, start_destination, end_destination, total_range_of_car):
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
    
    def breadth_first_search(start_destination):
        queue = Queue()
        queue.put(start_destination)
        
        while queue.qsize() > 0:
            current_node = queue.get()
            if current_node in edge_dictionary:
                for adjacent_node in edge_dictionary[current_node]:
                    if adjacent_node == end_destination:
                        return True
                    queue.put(adjacent_node)
        return False
    
    return breadth_first_search(start_destination)

graph = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
edge_weights = [((0, 1), 50), ((0, 2), 100), ((1, 3), 75), ((2, 3), 25), ((3, 4), 50)]
start_destination = 0
end_destination = 4
total_range_of_car = 100

print(path_exists(graph, edge_weights, start_destination, end_destination, total_range_of_car))
        

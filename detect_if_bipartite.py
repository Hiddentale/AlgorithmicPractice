from typing import List, Tuple
from queue import Queue
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2

def has_edges(current_node, edge_dictionary):
      return current_node in edge_dictionary  

def BreadthFirstSearch(graph: List[Tuple[int, int]]) -> bool:
    
    edge_dictionary = {}
    for node in graph:
        if node[0] not in edge_dictionary:
            edge_dictionary[node[0]] = []
        edge_dictionary[node[0]].append(node[1])
        
    color_dictionary = {}
    queue = Queue()
    entry_node = graph[0]
    queue.put(entry_node[0])
    color_dictionary[entry_node[0]] = Color.RED
    
    while queue.qsize() > 0:
        current_node = queue.get()
        if has_edges(current_node, edge_dictionary):
            current_node_color = color_dictionary[current_node]
            for adjacent_node in edge_dictionary[current_node]:
                queue.put(adjacent_node)
                if adjacent_node not in color_dictionary:
                    if current_node_color == Color.RED:
                        color_dictionary[adjacent_node] = Color.BLUE
                    else:
                        color_dictionary[adjacent_node] = Color.RED
                else:
                    if color_dictionary[adjacent_node] == current_node_color:
                        print("Algorithm failed, graph is unsuitable.")
                        return False
    print("Algorithm succeeded, graph is bipartite.")
    return True
                
input = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (4, 5),
    (3, 5)
]

BreadthFirstSearch(input)


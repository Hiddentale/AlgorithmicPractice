from typing import List, Tuple
from queue import Queue
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2

def BreadthFirstSearch(graph: List[Tuple[int, int]]) -> bool:
    
    Edge_dictionary = {}
    for node in graph:
        if node[0] not in Edge_dictionary:
            Edge_dictionary[node[0]] = []
        Edge_dictionary[node[0]].append(node[1])
        
    Color_dictionary = {}
    queue = Queue()
    entry_node = graph[0]
    queue.put(entry_node[0])
    Color_dictionary[entry_node[0]] = Color.RED
    
    while queue.qsize() > 0:
        print(Color_dictionary)
        current_node = queue.get()
        if current_node in Edge_dictionary:
            print("Bla")
            current_node_color = Color_dictionary[current_node]
            for adjacent_node in Edge_dictionary[current_node]:
                queue.put(adjacent_node)
                if adjacent_node not in Color_dictionary:
                    if current_node_color == Color.RED:
                        Color_dictionary[adjacent_node] = Color.BLUE
                    else:
                        Color_dictionary[adjacent_node] = Color.RED
                else:
                    if Color_dictionary[adjacent_node] == current_node_color:
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
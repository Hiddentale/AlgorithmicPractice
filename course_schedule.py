from queue import LifoQueue
from typing import List
from enum import Enum

class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

def canFinish(number_of_nodes: int, graph: List[List[int]]):

    def current_node_already_visited(current_node):
        return visited[current_node] == Color.YELLOW
    
    def current_node_already_completely_visited(current_node):
        return visited[current_node] == Color.GREEN
    
    def mark_current_node_as_visited(current_node):
        visited[current_node] = Color.YELLOW
    
    def cycle_has_been_detected():
        return False

    def adjacent_nodes(current_node):
        return edge_dictionary[current_node]
    
    def cycle_has_been_recursively_detected(adjacent_node):
        return not RecursiveDepthFirstSearch(adjacent_node)
    
    def mark_current_node_as_completely_visited(current_node):
        visited[current_node] = Color.GREEN

    edge_dictionary = {}
    for node in graph:
        if node[0] not in edge_dictionary:
            edge_dictionary[node[0]] = []
        edge_dictionary[node[0]].append(node[1])

    
    visited = [Color.RED] * number_of_nodes

    def RecursiveDepthFirstSearch(current_node):
        if current_node_already_visited(current_node):
            return cycle_has_been_detected()
        elif current_node_already_completely_visited(current_node):
            return True
        
        mark_current_node_as_visited(current_node)
        if current_node in edge_dictionary:
            for adjacent_node in adjacent_nodes(current_node):
                if cycle_has_been_recursively_detected(adjacent_node):
                    return cycle_has_been_detected()
        
        mark_current_node_as_completely_visited(current_node)
        return True
    
    for node in range(number_of_nodes):
        if not current_node_already_visited(node) and not current_node_already_completely_visited(node):
            if cycle_has_been_recursively_detected(node):
                return False
    return True
    

def test():

    print(canFinish(1, [[1,0]]))

test()



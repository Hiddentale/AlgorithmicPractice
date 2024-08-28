from queue import Queue
from typing import List

def preprocess_data(edges: List[List[int]]) -> dict:
    dictionary = {}
    for node, edge in edges:
            if node not in dictionary:
                dictionary[node] = []
            if edge not in dictionary:
                dictionary[edge] = []
            dictionary[edge].append(node)
            dictionary[node].append(edge)
    return dictionary

def BreadthFirstSearch(node, dictionary, explored):
    queue = Queue()
    queue.put(node)
    while queue.qsize() > 0:
        vertex = queue.get()
        if vertex in dictionary:
            for edge in dictionary[vertex]:
                if edge not in explored:
                    explored.add(edge)
                    queue.put(edge)

def count_connected_components(number_of_nodes: int, edges: List[List[int]]) -> int:

        graph_data = preprocess_data(edges)

        explored = set()
        number_of_connected_components = 0
        for node in range(0, number_of_nodes):
            if node not in explored:
                number_of_connected_components += 1
                explored.add(node)
                BreadthFirstSearch(node, graph_data, explored)

        return number_of_connected_components

number_of_nodes = 100
edges_list = [[0, 99], [1, 99], [2, 98], [3, 97], [4, 96], [5, 95], [6, 0], [7, 0], [8, 7], [9, 8], [9, 11]]

number_of_connected_components = count_connected_components(number_of_nodes, edges_list)
print(number_of_connected_components)
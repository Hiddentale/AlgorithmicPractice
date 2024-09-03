from typing import List
from queue import LifoQueue

def is_cyclic_graph(self, start: List[int], end: List[int]) -> bool:
        
        dictionary = {}
        for index, node in enumerate(start):
            if node not in dictionary:
                dictionary[node] = []
            dictionary[node].append(end[index])
        
        permanently_visited = {}
        
        for source_node in set(start):
            if source_node not in permanently_visited:

                stack = LifoQueue()
                source_node = start[0]
                stack.put((source_node, 0))
                
                while stack.qsize() > 0:
                    current_node, index = stack.get()

                    if current_node not in permanently_visited:
                        permanently_visited[current_node] = False

                    if index < len(dictionary.get(current_node, [])):
                        child_node = dictionary[current_node][index]
                        stack.put((current_node, index + 1))

                        if child_node in permanently_visited:
                            if permanently_visited.get(child_node) == False:
                                return True
                        else:
                            stack.put((child_node, 0))
                    else:
                        permanently_visited[current_node] = True
                return False
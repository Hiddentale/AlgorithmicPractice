from queue import LifoQueue


def DepthFirstSearch(graph, entry_node):
    
    stack = LifoQueue()
    stack.put(entry_node)

    visited = set()

    while stack.qsize() > 0:
        current_node = stack.get()
        if current_node not in visited:
            visited.add(current_node)
            for edge in graph[current_node]:
                 stack.put(edge)
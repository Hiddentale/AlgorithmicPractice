from queue import Queue

def BreadthFirstSearch(graph, entry_node, graph_width, graph_length, transformation_coordinates):

    queue = Queue()
    queue.put(entry_node)

    while queue.qsize() > 0:
        current_node = queue.get()
        graph[current_node[0]][current_node[1]] = "0"
        for element in graph:
            print(element)
        for transformation in transformation_coordinates:
            new_node = [a + b for a, b in zip(current_node, transformation)]
            if 0 <= new_node[0] < graph_width and 0 <= new_node[1] < graph_length and graph[new_node[0]][new_node[1]] == "1":
                queue.put(new_node)


def count_number_of_islands(graph):

    graph_width, graph_length = len(graph), len(graph[0])
    
    transformation_coordinates = ([1, 0], [0, 1], [-1, 0], [0, -1])

    number_of_islands = 0
    
    for i in range(graph_width):
        for j in range(graph_length):
            if graph[i][j] != "0":
                number_of_islands += 1
                BreadthFirstSearch(graph, [i, j], graph_width, graph_length, transformation_coordinates)
    
    return number_of_islands



input = [["0","1","0","1","0"],
         ["0","0","1","1","0"],
         ["1","1","0","1","0"],
         ["0","1","0","1","1"]]

print(count_number_of_islands(input))

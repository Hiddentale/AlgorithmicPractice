from typing import List, Tuple
from queue import Queue

possible_neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1]]

def BreadthFirstSearch(matrix, x, y, matrix_depth, matrix_length) -> bool:
    queue = Queue()
    current_region = (x, y)
    queue.put(current_region)
    
    while queue.qsize() > 0:
        current_x, current_y = queue.get()
        matrix[current_x][current_y] = 0
        possible_new_coordinates = [[current_x + coordinates[0], current_y + coordinates[1]] for coordinates in possible_neighbours]
        for neighbour in possible_new_coordinates:
            new_x, new_y = neighbour[0], neighbour[1]
            if 0 <= new_x < matrix_depth and 0 <= new_y < matrix_length and matrix[new_x][new_y] == 1:
                adjacent_region = (new_x, new_y)
                queue.put(adjacent_region)
                
def count_number_of_regions(matrix):
    
    number_of_regions = 0
    
    matrix_depth, matrix_length = len(matrix), len(matrix[0])
    
    for x in range(0, matrix_depth):
        for y in range(0, matrix_length):
            if matrix[x][y] == 1:
                
                number_of_regions += 1
                BreadthFirstSearch(matrix, x, y, matrix_depth, matrix_length)
                
    print(number_of_regions)
                
input = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]

count_number_of_regions(input)
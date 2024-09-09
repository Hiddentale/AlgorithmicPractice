from queue import Queue

def count_number_of_islands(map: list[list[str]]) -> int:

    number_of_islands = 0

    map_depth, map_length = len(map), len(map[0])


    def coordinates_are_valid(next_i, next_j):
        return 0 <= next_i < map_depth and 0 <= next_j < map_length

    for i in range(map_depth):
        for j in range(map_length):
            entry_node = map[i][j]
            if entry_node == "1":
                number_of_islands += 1

                queue = Queue()
                queue.put([i, j])
                map[i][j] = "0"

                while queue.qsize() > 0:
                    current_i, current_j = queue.get()
                    for d_i, d_j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                        next_i = current_i + d_i
                        next_j = current_j + d_j
                        if coordinates_are_valid(next_i, next_j) and map[next_i][next_j] == "1":
                            map[next_i][next_j] = "0"
                            queue.put([next_i, next_j])
            else:
                continue

    return number_of_islands

input = [["0","1","0","1","0"],
         ["0","0","0","1","0"],
         ["1","1","0","0","0"],
         ["0","1","0","1","1"]]

print(count_number_of_islands(input))
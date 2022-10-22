from typing import List, Tuple
import queue

"""This solutions uses BFS"""

def getNeighbours(row_count: int, col_count: int, coordinate: Tuple[int]) -> List[Tuple[int]]:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    neighbours = []
    for direction in directions:
        x = coordinate[0] + direction[0]
        y = coordinate[1] + direction[1]

        if 0 <= x < row_count and 0 <= y < col_count:
            neighbours.append((x, y))

    return neighbours


def numIslands(grid: List[List[str]]) -> int:
    count_island = 0

    row_count = len(grid)
    col_count = len(grid[0])

    q = queue.Queue(row_count * col_count)

    visited = [[False for j in range(col_count)] for i in range(row_count)]

    for i in range(row_count):
        for j in range(col_count):
            if visited[i][j] or grid[i][j] == "0": 
                continue

            q.put((i, j))
            visited[i][j] = True

            while not q.empty():
                current_coordinate = q.get()
                current_coordinate_x = current_coordinate[0]
                current_coordinate_y = current_coordinate[1]

                if grid[current_coordinate_x][current_coordinate_y] == "1":
                    neighbours = getNeighbours(row_count, col_count, current_coordinate)

                    for neighbour in neighbours:
                        x = neighbour[0]
                        y = neighbour[1]

                        if not visited[x][y]:
                            q.put(neighbour)    
                            visited[x][y] = True
            
            count_island += 1

    return count_island


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(numIslands(grid))
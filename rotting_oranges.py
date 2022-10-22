from typing import List, Tuple
import queue

def getNeighbours(node: Tuple[int], row_count: int, col_count: int) -> List[Tuple[int]]:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    neighbours = []
    for direction in directions:
        x = node[0] + direction[0]
        y = node[1] + direction[1]

        if 0 <= x < row_count and 0 <= y < col_count:
            neighbours.append((x, y))

    return neighbours


def orangesRotting(grid: List[List[int]]) -> int:
    row_count = len(grid)
    col_count = len(grid[0])
    minute = 0

    q = queue.Queue(row_count * col_count)

    # initialization
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j] == 2:
                q.put((i, j))

    visited = [[False for j in range(col_count)]for i in range(row_count)]

    while not q.empty():
        minute += 1
        q_size = q.qsize()

        for _ in range(q_size):
            node = q.get()
            neighbours = getNeighbours(node, row_count, col_count)

            x = node[0]
            y = node[1]
            visited[x][y] = True

            for neighbour in neighbours:
                x = neighbour[0]
                y = neighbour[1]
                
                if grid[x][y] == 1 and not visited[x][y]:
                    grid[x][y] = 2
                    q.put(neighbour)
        
    # check if there is any fresh orange
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j] == 1:
                return -1

    return max(0, minute - 1)


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
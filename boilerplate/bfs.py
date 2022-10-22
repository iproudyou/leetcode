from typing import List, Tuple
import queue

def getNeighbours(node: Tuple[int]) -> List[Tuple[int]]:
    return []

def solution():
    def bfs():
        row_count = 3
        col_count = 4

        q = queue.Queue(row_count * col_count)
        q.put((0, 0))

        visited = [[False for j in range(col_count) ]for i in range(row_count)]
        visited[0][0] = True

        while not q.empty():
            node = q.get()
            neighbours = getNeighbours(node)

            for neighbour in neighbours:
                q.put(neighbour)

                x = neighbour[0]
                y = neighbour[1]
                visited[x][y] = True
    

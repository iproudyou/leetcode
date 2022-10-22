import math
from typing import Tuple, List
from heapq import heappush, heappop

def euclidean_distance(p: Tuple[int]) -> float:
    x = p[0]
    y = p[1]
    return math.sqrt(x ** 2 + y ** 2)

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []

    for point in points:
        heappush(heap, (euclidean_distance(point), point))

    return [heappop(heap)[1] for i in range(k)]

points = [[1,3],[-2,2]]
k = 1

print(kClosest(points, k))
# min-heap
# heappush
# heappop
# heapify
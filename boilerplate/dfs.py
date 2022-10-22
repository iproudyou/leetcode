from typing import List, Dict
import collections

def build_adjacency_list(connections: List[List[int]]) -> Dict[int, List[int]]:
    adjacency_list = collections.defaultdict(list)

    for start, end in connections:
        adjacency_list[start].append(end)
        adjacency_list[end].append(start)

    return adjacency_list

def solution(n, connections):
    visited = [False for i in range(n)]
    adjacency_list = build_adjacency_list(connections)

    def dfs(at):
        if visited[at]:
            return
        
        visited[at] = True

        neighbours = adjacency_list[at]
        for neighbour in neighbours:
            dfs(neighbour)

from typing import List, Dict
import collections

NOT_VISITED = -2

def build_adjacency_list(n: int, connections: List[List[int]]) -> Dict[int, List[int]]:
    adjacency_list = collections.defaultdict(list)

    for start, end in connections:
        adjacency_list[start].append(end)
        adjacency_list[end].append(start)

    return adjacency_list


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    # 1. make adjancy list
    adjacency_list = build_adjacency_list(n, connections)

    # 2. build connections
    connections = set(map(tuple, map(sorted, connections)))
    
    # 3. initialize all nodes to -1
    ranks = [NOT_VISITED for i in range(n)]

    def dfs(at: int, depth: int) -> int:
        # already visited
        if ranks[at] != NOT_VISITED:
            return ranks[at]

        # update the depth
        ranks[at] = depth

        # recursion
        min_rank_overall = n

        if at in adjacency_list:
            children = adjacency_list[at]
            for child in children:
                if ranks[child] == depth - 1:
                    continue

                min_rank = dfs(child, depth + 1)

                # handle cycle for ancestors
                if ranks[at] >= min_rank:
                    connections.discard(tuple(sorted((at, child))))
                
                min_rank_overall = min(min_rank_overall, min_rank)

        return min_rank_overall
    
    dfs(0, 0)

    return list(connections)

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

print(criticalConnections(n, connections))


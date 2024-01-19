from typing import List
from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set(restricted)
        count = 0
        
        def dfs(node):
            nonlocal count
            visited.add(node)
            count += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return count

from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)

        def dfs(graph, source, destination, visited):
            if source == destination:
                return True
            if source in visited:
                return False
            visited.add(source)
            for neighbor in graph[source]:
                if dfs(graph, neighbor, destination, visited):
                    return True
            return False

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return dfs(graph, source, destination, visited)

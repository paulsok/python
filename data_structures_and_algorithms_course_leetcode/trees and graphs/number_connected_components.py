from typing import List
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        if not edges:
            return n
        
        def dfs(graph, visited, node):
            visited[node] = 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(graph, visited, neighbor)

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [0] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                dfs(graph, visited, i)
                ans += 1

        return ans

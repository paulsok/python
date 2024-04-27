from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        target_node = len(graph) - 1
        
        def backtrack(curr, path):
            if curr == target_node:
                paths.append(list(path))

            for next_node in graph[curr]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        
        backtrack(0, [0])

        return paths
        
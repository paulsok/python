from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(node):
            if node < 0 or node >= len(arr) or node in seen:
                return False
            
            if arr[node] == 0:
                return True
            
            seen.add(node)
            return dfs(node + arr[node]) or dfs(node - arr[node])
        
        seen = set()
        return dfs(start)

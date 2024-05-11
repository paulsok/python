from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def backtracking(val):
            if 10 ** (n - 1) <= val < 10 ** n:
                ans.append(val)
                return
            
            for i in range(10):
                if abs(val % 10 - i) == k:
                    backtracking(val * 10 + i)
        
        for i in range(1, 10):
            backtracking(i)
        return ans

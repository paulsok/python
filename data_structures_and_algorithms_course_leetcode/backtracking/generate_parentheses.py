from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(cur, left, right):
            if len(cur) == 2 * n:
                ans.append("".join(cur))
                return
            
            if left < n:
                cur.append("(")
                backtracking(cur, left + 1, right)
                cur.pop()
    
            if right < left:
                cur.append(")")
                backtracking(cur, left, right + 1)
                cur.pop()

        backtracking([], 0, 0)
        return ans

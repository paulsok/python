from typing import List
from functools import cache


# This is the recursive version of the solution
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            
            j = i + questions[i][1] + 1
            return max(questions[i][0] + dp(j), dp(i + 1))
    
        return dp(0)
    

# This is the iterative version of the above solution
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1) # n + 1 to avoid out of bounds
        
        for i in range(n - 1, -1, -1):
            j = i + questions[i][1] + 1
            # need to make sure we don't go out of bounds
            dp[i] = max(questions[i][0] + dp[min(j, n)], dp[i + 1])
        
        return dp[0]

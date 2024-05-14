from typing import List


# Top-down approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. A function that returns the answer
        def dp(i):
            if i <= 1:
                # 3. Base cases
                return 0
            
            if i in memo:
                return memo[i]
            
            # 2. Recurrence relation
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))


# Bottom-up approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Step 2
        dp = [0] * (n + 1)
        
        # Step 3: Base cases are implicitly defined as they are 0

        # Step 4
        for i in range(2, n + 1):
            # Step 5
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        # Step 6
        return dp[n]

from typing import List


# Top-down approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            # to prevent out of bounds error
            return nums[0]
        
        def dp(i):
            # Base cases
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            # Recurrence relation
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        
        memo = {}
        return dp(len(nums) - 1)
    

# Bottom-up approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        # To avoid out of bounds error from setting base case
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            # Recurrence relation
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n - 1]


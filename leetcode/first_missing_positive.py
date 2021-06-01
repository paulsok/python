# Example 1:
# Input: nums = [1,2,0]
# Output: 3

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            if abs(nums[i]) > n:
                continue
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums = set(nums)
        for i in range(nums_len + 1):
            if i not in nums:
                return i

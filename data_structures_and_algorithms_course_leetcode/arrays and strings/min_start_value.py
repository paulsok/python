from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = temp = nums[0]
        for num in nums[1:]:
            temp += num
            startValue = min(temp, startValue)
        return max(1, 1 - startValue)

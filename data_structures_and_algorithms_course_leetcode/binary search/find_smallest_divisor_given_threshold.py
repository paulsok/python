from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = -1
        lowest = 1
        higthes = max(nums)

        def division_sum(divisor):
            division_sum = 0
            for num in nums:
                division_sum += ceil(num/divisor)
            return division_sum

        while lowest <= higthes:
            middle = (lowest+higthes) // 2
            result = division_sum(middle)

            if result <= threshold:
                ans = middle
                higthes = middle - 1
            else:
                lowest = middle + 1

        return ans

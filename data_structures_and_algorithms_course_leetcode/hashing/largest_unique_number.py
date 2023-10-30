from typing import List
from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        default_dict = defaultdict(int)

        for num in nums:
            default_dict[num] += 1

        ans = -1
        for key in default_dict:
            if default_dict[key] == 1 and key > ans:
                ans = key
        return ans

from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)
        
        ans = sum_num = 0
        for pair in ordered:
            sum_num += pair
            ans += 1
            if sum_num >= len(arr) // 2:
                break

        return ans

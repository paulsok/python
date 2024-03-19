import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 0:
            return 0
        
        heapq.heapify(sticks)
        ans = 0
        
        while len(sticks) > 1:
            total_sum = heapq.heappop(sticks) + heapq.heappop(sticks)
            ans += total_sum
            heapq.heappush(sticks, total_sum)
            
        return ans

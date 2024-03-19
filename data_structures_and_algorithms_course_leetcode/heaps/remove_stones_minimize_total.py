import heapq
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for _ in range(k):
            largest = -heapq.heappop(piles)
            heapq.heappush(piles, -(largest-floor(largest/2)))
        return -sum(piles)

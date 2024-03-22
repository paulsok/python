import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            distance = - sqrt(point[0]**2+point[1]**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, point))
            else:
                heapq.heappush(heap, (distance, point))
        
        return [point[1] for point in heap]

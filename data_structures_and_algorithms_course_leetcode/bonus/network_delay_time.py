from math import inf
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for x, y, z in times:
            graph[x - 1].append([y - 1, z])

        distances = [inf] * n
        distances[k - 1] = 0
        heap = [(0, k - 1)]
        while heap:
            curr_dist, node = heappop(heap)
            if curr_dist > distances[node]:
                continue

            for nei, weight in graph[node]:
                dist = curr_dist + weight
                if dist < distances[nei]:
                    distances[nei] = dist
                    heappush(heap, (dist, nei))

        ans = max(distances)
        return ans if ans < inf else -1

import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i:[] for i in range(n)}

        for frm, to, price in flights:
            adj_list[frm].append((to, price))

        best_visited = [2**31] * n

        prior_queue = [ (0, -1, src) ]  #  weight, steps, node

        while prior_queue:
            cost, steps, node = heapq.heappop(prior_queue)

            if best_visited[node] <= steps:
                continue

            if steps > k:
                continue

            if node == dst:
                return cost

            best_visited[node] = steps

            for neighbour, weight in adj_list[node]:
                heapq.heappush(prior_queue, (cost + weight, steps + 1, neighbour))

        return -1

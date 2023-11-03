from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_stones = defaultdict(int)

        for stone in stones:
            if stone in jewels:
                jewels_stones[stone] += 1

        return sum(jewels_stones.values())

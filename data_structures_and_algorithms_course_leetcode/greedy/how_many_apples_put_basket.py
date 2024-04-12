from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        basket = sorted(arr)
        apples = units = 0

        for weight in basket:
            units += weight
            if units > 5000:
                break
            apples += 1

        return apples

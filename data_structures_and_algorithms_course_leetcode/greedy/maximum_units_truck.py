from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ordered = sorted(boxTypes, key=lambda x:x[1], reverse=True)

        size = 0
        for n, items in ordered:
            box = min(n, truckSize)
            size += box * items
            truckSize -= box
            
            if truckSize == 0:
                break

        return size
        
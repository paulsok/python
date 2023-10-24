from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        ans = {}
        set_arr = set(arr)

        for num in arr:
            if num + 1 in set_arr and num not in ans.keys():
                ans[num] = 1
            elif num + 1 in set_arr:
                ans[num] += 1

        return sum(ans.values())

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(store, combination, next_n):
            if store == 0 and len(combination) == k:
                ans.append(list(combination))
                return
            if store < 0 or len(combination) == k:
                return

            for i in range(next_n, 9):
                combination.append(i + 1)
                backtrack(store - i - 1, combination, i + 1)
                combination.pop()

        backtrack(n, [], 0)

        return ans

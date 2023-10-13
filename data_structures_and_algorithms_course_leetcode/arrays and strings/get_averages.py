from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        ans = [-1] * n

        if 2 * k + 1 > n:
            return ans

        prefix = [nums[0]]
        for num in nums:
            prefix.append(num + prefix[-1])

        for i in range(k, n - k):
            ans[i] = int((prefix[i + k + 1] - prefix[i - k]) / (k * 2 + 1))
        return ans

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            x = target - num
            if x not in temp:
                temp[num] = i
            else:
                return [temp[x], i]

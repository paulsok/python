# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            x = target - num
            if x not in temp:
                temp[num] = i
            else:
                return [temp[x], i]

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            result = [p[:i] + [n] + p[i:] for p in result
                      for i in range((p + [n]).index(n) + 1)]

        return result

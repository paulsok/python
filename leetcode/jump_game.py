# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution:
    def jump(self, array: List[int]) -> int:
        min_jumps = [float("inf") for _ in array]
        min_jumps[0] = 0

        for i in range(1, len(array)):
            for idx in range(i):
                if array[idx] >= (i - idx):
                    min_jumps[i] = min(min_jumps[i], min_jumps[idx] + 1)

        return min_jumps[-1]

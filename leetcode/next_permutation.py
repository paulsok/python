# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        while i > -1:
            if nums[i] < nums[i+1]:
                next = j = i + 1

                while j < len(nums) and nums[i] < nums[j]:
                    next = j
                    j += 1

                nums[i], nums[next] = nums[next], nums[i]
                break

            i -= 1

        nums[i+1:] = nums[i+1:][::-1]

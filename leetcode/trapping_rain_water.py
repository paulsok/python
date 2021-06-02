# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section)
# is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= l_max:
                    l_max = height[left]
                else:
                    answer += l_max - height[left]
                left += 1

            else:
                if height[right] >= r_max:
                    r_max = height[right]
                else:
                    answer += r_max - height[right]
                right -= 1

        return answer

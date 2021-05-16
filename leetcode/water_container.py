# Input: height = [4,3,2,1,4]
# Output: 16

class Solution:
    def maxArea(self, height):
        max_area = 0
        i, j = 0, len(height) - 1

        while i < j:
            max_area = max(min(height[i], height[j]) * (j - i), max_area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_area

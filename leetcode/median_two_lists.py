# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new_list = sorted(nums1 + nums2)
        lenght = len(new_list)
        ind = lenght // 2

        if lenght % 2:
            return new_list[ind]

        return (new_list[ind-1] + new_list[ind]) / 2.0

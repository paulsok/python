class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new_list = sorted(nums1 + nums2)
        lenght = len(new_list)
        ind = lenght // 2

        if lenght % 2:
            return new_list[ind]

        return (new_list[ind-1] + new_list[ind]) / 2.0

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def merge(nums1,nums2):
            ptr1,ptr2 = 0, 0
            result = []
            while ptr1 < len(nums1) and ptr2 < len(nums2):
                if nums1[ptr1] <= nums2[ptr2]:
                    value = nums1[ptr1]
                    ptr1 += 1
                else:
                    value = nums2[ptr2]
                    ptr2 += 1
                result.append(value)
            result.extend(nums1[ptr1:]+nums2[ptr2:])
            return result
        merged = merge(nums1,nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2] + merged[n//2 - 1])/2
        return merged[n//2]


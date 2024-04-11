class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged = []
        m,n = len(nums1), len(nums2)
        ptr1, ptr2 = 0, 0

        def fun(merged,ptr1,ptr2):

            if ptr1 >= m:
                
                merged.extend(nums2[ptr2:])

                return merged
            
            if ptr2 >= n:

                merged.extend(nums1[ptr1:])

                return merged
            
            if nums1[ptr1] <= nums2[ptr2]:

                value = nums1[ptr1]
                ptr1 += 1
            
            else:

                value = nums2[ptr2]
                ptr2 += 1
            
            merged.append(value)

            return fun(merged,ptr1,ptr2)

        merged = fun(merged,ptr1,ptr2)

        mid = (m+n-1)//2

        if (m + n) %2 == 0:

            return (merged[mid] + merged[mid+1])/2
        
        else:

            return merged[mid]
            




                

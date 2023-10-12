class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(len(nums2)):
            nums1[m+i] = nums2[i]
       
        for i in range(len(nums1)):

            key = nums1[i]
            j = i - 1

            while j >= 0 and key < nums1[j]:

                nums1[j+1] = nums1[j]
                j -= 1

            nums1[j+1] = key
        
        class Solution:
    
        # i = m - 1
        # j = n - 1
        # k = m + n - 1

        # while j >= 0:

        #     if i >=0 and nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1

        #     k -= 1

        
        

        
        

        

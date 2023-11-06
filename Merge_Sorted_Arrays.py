class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """

        i = m-1
        j = n-1
        k = 0
        length = len(nums1)

        while i >= 0 and j >= 0:

            if nums2[j] >= nums1[i]:

                nums1[length-k-1] = nums2[j]
                j -= 1
            
            elif nums2[j] < nums1[i]:

                nums1[length-k-1] = nums1[i]
                i -= 1
            
            k += 1
        
        if i < 0:

            nums1[:length-k] = nums2[:j+1]

     #######################################################       

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

    ##############################################################
    
        # nums1[m:] = nums2

        # n = len(nums1)

        # for i in range(1,n):

        #     j = i - 1
        #     key = nums1[i]

        #     while j >= 0 and key < nums1[j]:

        #         nums1[j+1] = nums1[j]
        #         j -= 1
            
        #     nums1[j+1] = key

        
        

        

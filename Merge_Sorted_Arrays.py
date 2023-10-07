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
        
        print(nums1)
        

        

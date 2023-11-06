class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        lists = []

        for i in range(len(nums1)):

            flag = False

            start = nums2.index(nums1[i]) + 1

            for j in range(start,len(nums2)):

                if nums1[i] < nums2[j]:

                    flag = True
                    lists.append(nums2[j])
                    break
            
            if not flag:
                lists.append(-1)

        
        return lists




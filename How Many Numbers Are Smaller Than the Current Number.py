class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = sorted(nums)
        nums2 = nums
        lists = []
        i, j = 0, 0
        while j < len(nums2):
            if nums2[j] > nums1[i]:
                i+=1
                if i == len(nums1):
                    i = 0
                    j+=1
            else:
                lists.append(i)
                i = 0
                j += 1
        return lists

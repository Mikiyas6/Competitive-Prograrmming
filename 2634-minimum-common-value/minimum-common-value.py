class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        set1 = set(nums1)
        set2 = set(nums2)

        set3 = set1.intersection(set2)

        set3 = list(set3)

        set3.sort()

        return set3[0] if set3 else -1

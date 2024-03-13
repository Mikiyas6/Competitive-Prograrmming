class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                merged.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                merged.append([id1, val1])
                i += 1
            else:
                merged.append([id2, val2])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged
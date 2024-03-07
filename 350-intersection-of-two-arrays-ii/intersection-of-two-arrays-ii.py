class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap1 = Counter(nums1)
        hashmap2 = Counter(nums2)

        output = []

        for value in nums1:

            if value in hashmap2:

                output.append(value)

                hashmap2[value] -= 1

                if not hashmap2[value]:

                    del hashmap2[value]

        return output
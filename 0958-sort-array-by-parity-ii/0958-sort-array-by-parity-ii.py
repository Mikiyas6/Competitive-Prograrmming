class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even = [value for value in nums if value %2 == 0]
        odd = [value for value in nums if value %2 != 0]

        ptr1, ptr2 = 0, 0
        results = []
        while ptr1 < len(even) and ptr2 < len(odd):

            results.extend([even[ptr1],odd[ptr2]])
            ptr1 += 1
            ptr2 += 1
        
        return results
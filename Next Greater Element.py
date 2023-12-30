class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        monotonic_stack = []

        result = [-1] * len(nums1)

        hashmap = defaultdict(int)

        for index, value in enumerate(nums1):

            hashmap[value] = index
        
        for value in nums2:

            while monotonic_stack and value > monotonic_stack[-1]:

                removed = monotonic_stack.pop()

                result[hashmap[removed]] = value
            
            if value in hashmap:

                monotonic_stack.append(value)
        
        return result


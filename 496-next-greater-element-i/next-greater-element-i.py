class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = defaultdict(int)

        for index, value in enumerate(nums1):

            hashmap[value] = index
        
        stack = []
        result = [0]*len(nums1)

        for value in nums2:

            while stack and value > stack[-1]:

                popped = stack.pop()
                index = hashmap[popped]
                result[index] = value
            
            if value in hashmap:

                stack.append(value)
        
        for index, value in enumerate(result):

            if value == 0:

                result[index] = -1
        
        return result
            
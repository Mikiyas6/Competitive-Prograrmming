class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = defaultdict(int)

        for index,value in enumerate(nums1):

            hashmap[value] = index
        
        stack = []
        output = [0] * len(nums1)

        for value in nums2:

            while stack and value > stack[-1]:

                removed = stack.pop()

                if removed in hashmap:

                    output[hashmap[removed]] = value
            
            stack.append(value)
        
        for index,value in enumerate(output):

            if value == 0:

                output[index] = -1
            
        return output
        
        


        

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        stack = []
        hashmap = defaultdict(int)
        for value in nums2:
            while stack and value > stack[-1]:
                popped_value = stack.pop()
                hashmap[popped_value] = value
            stack.append(value)
        for index,value in enumerate(nums1):
            if hashmap[value]:
                result[index] = hashmap[value]
        return result 
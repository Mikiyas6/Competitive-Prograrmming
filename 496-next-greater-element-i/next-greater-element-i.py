class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = defaultdict(int)
        for value in nums2:
            while stack and value > stack[-1]:
                popped = stack.pop()
                hashmap[popped] = value
            stack.append(value)
        result = []
        for value in nums1:
            result.append(hashmap[value] if hashmap[value] else -1) 
        return result


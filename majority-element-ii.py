class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        occurance = n // 3

        hashmap = Counter(nums)

        output = []

        for value in hashmap:

            if hashmap[value] > occurance:

                output.append(value)
        
        return output

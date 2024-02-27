class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)

        appearance = n//3
        
        hashmap = Counter(nums)

        output = [number for number, occurance in hashmap.items() if occurance > appearance]

        return output
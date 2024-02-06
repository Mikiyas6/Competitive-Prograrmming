class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashmap = Counter(nums)

        for num in hashmap:

            if hashmap[num] == 1:

                return num

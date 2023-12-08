class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = defaultdict(int)

        for i in range(len(nums)):

            if nums[i] in hashmap:

                return True
            
            hashmap[nums[i]] = i
        
        return False

        # n = len(nums)

        # nums.sort()

        # i = 0
        # j = i + 1


        # while j < n:

        #     if nums[i] == nums[j]:

        #         return True
            
        #     i += 1
        #     j += 1
            
        # return False

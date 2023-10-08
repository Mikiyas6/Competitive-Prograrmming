class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        new_set = set()

        for k in range(len(nums)):

            key = nums[k]
            i = k+1
            j = len(nums) - 1

            while i < j:

                total = key + nums[i] + nums[j]

                if total == 0:

                    new_set.add((key,nums[i],nums[j]))

                    i += 1
                    j -= 1
                
                elif total > 0:

                    j -= 1

                else:

                    i += 1 

        lists = [list(value) for value in new_set]

        return lists

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        hashset = set()

        n = len(nums)

        for k in range(n):

            target_number = nums[k]

            complement_target_number = -1 * target_number

            i = k + 1
            j = n - 1

            while i < j:

                total = nums[i] + nums[j]

                if total == complement_target_number:

                    hashset.add((target_number,nums[i],nums[j]))

                    i += 1
                    j -= 1
                
                elif total < complement_target_number:

                    i += 1
                
                else:

                    j -= 1

        output = [list(value) for value in hashset]

        return output


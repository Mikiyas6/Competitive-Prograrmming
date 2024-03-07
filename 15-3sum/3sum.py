class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        n = len(nums)

        output = set()

        for index, value in enumerate(nums):

            if value > 0:

                continue

            left = index + 1
            right = n - 1

            target = -1 * value

            while left < right:

                total = nums[left] + nums[right]

                if total < target:

                    left += 1
                
                elif total > target:

                    right -= 1
                
                else:

                    output.add((value,nums[left],nums[right]))
                    left += 1
                    right -= 1
        
        result = [list(items) for items in output]
        return result


        # for k in range(n):

        #     i = k + 1
        #     j = n - 1

        #     complement = -1 * nums[k]

        #     while i < j:

        #         summation = nums[i] + nums[j]

        #         if summation == complement:

        #             hashset.add((nums[k],nums[i],nums[j]))
        #             i += 1
        #             j -= 1
                
        #         elif summation < complement:

        #             i += 1
                
        #         else:

        #             j -= 1
            
        # output = list(map(list,hashset))

        # return output


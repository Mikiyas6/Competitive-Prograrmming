class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        n = len(nums)

        output = set()

        for index, value in enumerate(nums):

            new_target = target - value

            for i in range(index+1,n):

                newest_target = new_target - nums[i]

                left = i + 1
                right = n - 1

                while left < right:

                    if nums[left] + nums[right] < newest_target:

                        left += 1
                    
                    elif nums[left] + nums[right] > newest_target:

                        right -= 1
                    
                    else:

                        output.add((value,nums[i],nums[left],nums[right]))

                        left += 1
                        right -= 1
            
        result = list(map(list,output))

        result.sort()

        return result
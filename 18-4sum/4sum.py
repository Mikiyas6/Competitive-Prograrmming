class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        result=set()
        nums.sort()
        l=0
        while l<len(nums)-3:
            t=target-nums[l]
            j=l+1
            while j<len(nums)-2:
                tt=t-nums[j]
                z=j+1
                r=len(nums)-1
                while z<r:
                    if nums[z]+nums[r]==tt:
                        result.add((nums[l],nums[j],nums[z],nums[r]))
                        while z < r and nums[z] == nums[z+1]:
                            z += 1
                        while z < r and nums[r] == nums[r-1]:
                            r -= 1
                        z += 1
                        r -= 1
                    elif nums[z]+nums[r]>tt:
                        r-=1
                    else:
                        z+=1
                j+=1
            l+=1
        return result

        # # nums = [2, 2,   2,2]    target = 8
        
        # nums.sort()

        # n = len(nums)

        # output = set()

        # for index, value in enumerate(nums):

        #     new_target = target - value # new_target = 8 - 2 = 6

        #     for i in range(index+1,n):

        #         newest_target = new_target - nums[i] # newest_target = 6 - 2 = 4

        #         left = i + 1
        #         right = n - 1

        #         while left < right:

        #             if nums[left] + nums[right] < newest_target:

        #                 left += 1
                    
        #             elif nums[left] + nums[right] > newest_target:

        #                 right -= 1
                    
        #             else:

        #                 output.add((value,nums[i],nums[left],nums[right]))

        #                 left += 1
        #                 right -= 1
            
        # result = list(map(list,output))

        # result.sort()

        # return result
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()

        l = 0

        max_perimeter = 0

        for r in range(2,len(nums)):

            sum_of_two_sides = nums[l] + nums[l+1]

            if sum_of_two_sides <= nums[r]:

                l += 1

                continue 
            
            max_perimeter = max(max_perimeter,sum_of_two_sides + nums[r])

            l += 1
        
        return max_perimeter


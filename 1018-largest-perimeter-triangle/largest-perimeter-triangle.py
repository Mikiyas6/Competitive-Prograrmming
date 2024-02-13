class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()

        l = 0

        max_perimeter = 0

        sum_of_three_sides = sum(nums[:3])

        if sum_of_three_sides - nums[2] > nums[2]:

            max_perimeter = max(max_perimeter, sum_of_three_sides)

        for r in range(3,len(nums)):

            sum_of_three_sides -= nums[l]

            sum_of_three_sides += nums[r]

            if sum_of_three_sides - nums[r] > nums[r]:

                max_perimeter = max(max_perimeter,sum_of_three_sides) 

            l += 1
        
        return max_perimeter


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def fun(left,right):

            if left == right:
                return nums[left]
            
            left_side = nums[left] - fun(left+1,right)
            right_side = nums[right] - fun(left,right-1)

            return max(left_side,right_side)

        result = fun(0,len(nums)-1)

        return True if result >= 0 else False


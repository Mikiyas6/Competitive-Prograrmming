class Solution:
    def numberOfSteps(self, num: int) -> int:
        def helper(num,count):
            if num == 0:
                return count
            elif num %2 == 0:
                return helper(num/2,count+1)
            else:
                return helper(num-1,count+1)
        return helper(num,0)

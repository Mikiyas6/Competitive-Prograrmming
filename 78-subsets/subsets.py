class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []

        def backtrack(start,path):
            result.append(path[:])
            if start == n:
                return
            for i in range(start,n):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return result
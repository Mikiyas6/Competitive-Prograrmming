class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(i,path):
            result.append(path[:])
            if i >= n:
                return
            for j in range(i,n):
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()
        backtrack(0,[])
        return result
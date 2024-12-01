class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def backtrack(path):
            if len(path) == n:
                result.append(path[:])
                return
            for i in range(n):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
        backtrack([])
        return result
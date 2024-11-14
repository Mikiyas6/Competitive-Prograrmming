class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(nums,path):

            if len(path) == len(nums):
                result.append(path[:])
                return 
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(nums,path)
                    path.pop()
            
        backtrack(nums,[])
        return result

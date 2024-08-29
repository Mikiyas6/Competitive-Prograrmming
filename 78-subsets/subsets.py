class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        result = []
        k = int(math.pow(2,N))
        for i in range(k):
            subset = []
            for j in range(N):
                if (i & 1 << j):
                    subset.append(nums[j])
            result.append(subset)
        return result

        # def fun(i,subset):

        #     if i == len(nums):

        #         return [subset]
            
        #     return fun(i+1,subset+[nums[i]]) + fun(i+1,subset)
        
        # return fun(0,[])
            
            



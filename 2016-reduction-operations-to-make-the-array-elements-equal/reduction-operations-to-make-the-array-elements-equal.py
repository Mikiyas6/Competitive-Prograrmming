class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        unique_nums = sorted(freq.keys())
        operations = 0
        while len(unique_nums) > 1:
            largest = unique_nums.pop()
            next_largest = unique_nums[-1]
            operations += freq[largest]
            freq[next_largest] += freq[largest]
        
        return operations

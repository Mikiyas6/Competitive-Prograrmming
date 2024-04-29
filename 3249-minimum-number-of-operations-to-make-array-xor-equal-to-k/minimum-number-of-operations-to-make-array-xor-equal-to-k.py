class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        operations = 0
        for i in range(32):  
            if (k >> i) & 1 != (xor >> i) & 1:
                operations += 1
        
        return operations
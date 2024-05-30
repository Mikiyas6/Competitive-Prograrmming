class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXor = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefixXor[i] = prefixXor[i - 1] ^ arr[i - 1]
        
        count = 0
        
        for i in range(n):
            for k in range(i + 1, n):
                if prefixXor[i] == prefixXor[k + 1]:
                    count += (k - i)
        
        return count
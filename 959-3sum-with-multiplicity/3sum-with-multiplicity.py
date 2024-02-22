class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        MOD = 10**9 + 7
        count = 0
        freq = {}
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                complement = target - arr[i] - arr[j]
                if complement in freq and freq[complement] > 0:
                    count += freq[complement]
                    count %= MOD
                    
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        
        return count % MOD
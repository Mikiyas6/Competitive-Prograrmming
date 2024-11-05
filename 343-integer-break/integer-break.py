class Solution(object):
    def integerBreak(self, n):
        arr = [1] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                arr[i] = max(arr[i], max(arr[j], j) * (i - j))
        
        return arr[n]
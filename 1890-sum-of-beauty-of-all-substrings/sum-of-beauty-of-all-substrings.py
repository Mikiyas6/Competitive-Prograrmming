class Solution:
    def beautySum(self, s: str) -> int:
        
        n = len(s)
        total_beauty = 0
        
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                most_freq = max(freq)
                least_freq = min(count for count in freq if count > 0)
                total_beauty += most_freq - least_freq
        
        return total_beauty
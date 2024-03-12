class Solution:
    def minimumSteps(self, s: str) -> int:
        
        n = len(s)
        white_count = s.count('0')
        black_count = 0
        result = 0

        for i in range(n):
            if s[i] == '0':
                white_count -= 1
            else:
                result += white_count

        return result
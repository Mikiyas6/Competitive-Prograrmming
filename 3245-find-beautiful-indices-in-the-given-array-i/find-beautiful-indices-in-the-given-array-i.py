class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        len_a, len_b = len(a), len(b)
        result = []
        
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[i:i + len_a] == a:
                j = max(j, i - k)
                while j < len(s) and j <= i + k:
                    if s[j:j + len_b] == b and abs(j - i) <= k:
                        result.append(i)
                        break
                    j += 1
            i += 1
        
        return result

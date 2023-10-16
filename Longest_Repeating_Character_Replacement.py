class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        dictionary = {}
        max_frequency = 0

        for r in range(len(s)):

            dictionary[s[r]] = 1 + dictionary.get(s[r],0)
            max_frequency = max(max_frequency,dictionary[s[r]])
            diff = ( r - l + 1) - max_frequency

            while diff > k:

                dictionary[s[l]] -= 1
                l += 1
                diff = ( r - l + 1) - max_frequency

            res = max(res, r - l + 1)
        
        return res



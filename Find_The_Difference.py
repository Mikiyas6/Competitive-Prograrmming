class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hashmap_s = Counter(s)
        hashmap_t = Counter(t)
        
        for letter in t:

            if letter not in s or hashmap_s[letter] != hashmap_t[letter]:

                return letter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset = set()
        hashmap = defaultdict(str)
        for i in range(len(s)):
            if hashmap[s[i]]:
                if t[i] != hashmap[s[i]]:
                    return False
            else:
                if t[i] in hashset:
                    return False
                hashmap[s[i]] = t[i]
                hashset.add(t[i])
        return True

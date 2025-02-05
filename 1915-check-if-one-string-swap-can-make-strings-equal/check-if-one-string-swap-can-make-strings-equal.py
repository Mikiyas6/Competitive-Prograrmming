class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        hashmap1 = Counter(s1)
        hashmap2 = Counter(s2)
        for value in s1:
            if value not in hashmap2 or hashmap1[value] != hashmap2[value]:
                return False
        _hashmap1 = defaultdict(int)
        _hashmap2 = defaultdict(int)
        counter = 0
        for i in range(len(s1)):
            _hashmap1[s1[i]] = i
            _hashmap2[s2[i]] = i
            if s1[i] != s2[i]:
                counter += 1
                if counter > 2:
                    return False
        return True

















        candidates = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                candidates.append([s1[i],s2[i]])
                if len(candidates) > 2:
                    return False
        if len(candidates) < 2:
            return False
        print(candidates)
        if candidates[0][0] in candidates[1] and candidates[0][1] in candidates[1]:
            return True
        return False
                
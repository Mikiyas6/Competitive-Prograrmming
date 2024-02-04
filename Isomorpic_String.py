class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_mapping = defaultdict(str)
        t_to_s_mapping = defaultdict(str)

        for i in range(len(s)):
            if s[i] not in s_to_t_mapping:
                s_to_t_mapping[s[i]] = t[i]
            else:
                if s_to_t_mapping[s[i]] != t[i]:
                    return False

            if t[i] not in t_to_s_mapping:
                t_to_s_mapping[t[i]] = s[i]
            else:
                if t_to_s_mapping[t[i]] != s[i]:
                    return False

        return True

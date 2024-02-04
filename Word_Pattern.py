class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hashmap_pattern = defaultdict(str)
        hashmap_s = defaultdict(str)

        s_list = s.split(" ")

        if len(pattern) != len(s_list):

            return False

        for i in range(len(s_list)):

            if pattern[i] not in hashmap_pattern:

                hashmap_pattern[pattern[i]] = s_list[i]
            
            else:

                if hashmap_pattern[pattern[i]] != s_list[i]:

                    return False

            
            if s_list[i] not in hashmap_s:

                hashmap_s[s_list[i]] = pattern[i]

            else:

                if hashmap_s[s_list[i]] != pattern[i]:

                    return False

        return True
        


        
        
        



from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []

        p_hashmap = Counter(p)

        i = 0
        j = len(p)
        lists = []

        string = s[i:j]
        string_hashmap = Counter(string)

        if p_hashmap == string_hashmap:
            lists.append(i)
        
        i += 1
        j += 1
        
        while j < len(s)+1:

            string_hashmap[s[i-1]] -= 1
            string_hashmap[s[j-1]] += 1

            if string_hashmap == p_hashmap:

                lists.append(i)
            
            i += 1
            j += 1
        
        return lists

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:

#         from collections import Counter

#         dictionary = Counter(p)
        
#         i, j = 0, len(p)
#         lists = []

#         while j < len(s)+1:

#             string = s[i:j] 
#             new_dictionary = Counter(string)

#             if new_dictionary == dictionary:
#                 lists.append(i)

#             i += 1
#             j += 1

#         return lists
            

        
